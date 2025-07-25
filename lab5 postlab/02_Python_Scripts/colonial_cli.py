import sqlite3
import os
from textwrap import dedent

DB_PATH = r"C:\Users\User\Desktop\Repository\Lab 5 PostLab\04_DB\sqlite\colonial.db"

def print_table(headers, rows, max_rows=None):
    if max_rows is not None:
        rows = rows[:max_rows]
    widths = [len(h) for h in headers]
    for r in rows:
        for i, c in enumerate(r):
            widths[i] = max(widths[i], len(str(c)))
    fmt = " | ".join("{:<" + str(w) + "}" for w in widths)
    line = "-+-".join("-" * w for w in widths)
    print(fmt.format(*headers))
    print(line)
    for r in rows:
        print(fmt.format(*[str(c) for c in r]))
    print(f"\n{len(rows)} row(s)\n")

def run_query(conn, sql, params=(), title=None, max_rows=None):
    cur = conn.cursor()
    cur.execute(sql, params)
    rows = cur.fetchall()
    headers = [d[0] for d in cur.description]
    if title:
        print(f"\n=== {title} ===")
    print_table(headers, rows, max_rows=max_rows)

def show_guide(conn):
    run_query(conn, "SELECT * FROM GUIDE ORDER BY GUIDE_NUM;", title="GUIDE")

def show_customer(conn):
    run_query(conn, "SELECT * FROM CUSTOMER ORDER BY CUSTOMER_NUM;", title="CUSTOMER")

def show_trip(conn):
    run_query(conn, "SELECT * FROM TRIP ORDER BY TRIP_ID;", title="TRIP")

def show_reservation(conn):
    run_query(conn, "SELECT * FROM RESERVATION ORDER BY RESERVATION_ID;", title="RESERVATION")

def show_trip_guides(conn):
    run_query(conn, "SELECT * FROM TRIP_GUIDES ORDER BY TRIP_ID, GUIDE_NUM;", title="TRIP_GUIDES")

def report_reservations_with_customer_and_trip(conn):
    sql = dedent("""
        SELECT r.RESERVATION_ID,
               r.TRIP_ID,
               t.TRIP_NAME,
               r.TRIP_DATE,
               r.NUM_PERSONS,
               r.TRIP_PRICE,
               r.OTHER_FEES,
               r.CUSTOMER_NUM,
               c.LAST_NAME || ', ' || c.FIRST_NAME AS Customer
        FROM RESERVATION r
        JOIN TRIP t        ON t.TRIP_ID = r.TRIP_ID
        JOIN CUSTOMER c    ON c.CUSTOMER_NUM = r.CUSTOMER_NUM
        ORDER BY r.TRIP_DATE, r.RESERVATION_ID;
    """)
    run_query(conn, sql, title="Reservation Details (with Trip & Customer)")

def report_trip_with_guides(conn):
    sql = dedent("""
        SELECT t.TRIP_ID,
               t.TRIP_NAME,
               GROUP_CONCAT(g.FIRST_NAME || ' ' || g.LAST_NAME, ', ') AS Guides
        FROM TRIP t
        LEFT JOIN TRIP_GUIDES tg ON tg.TRIP_ID = t.TRIP_ID
        LEFT JOIN GUIDE g        ON g.GUIDE_NUM = tg.GUIDE_NUM
        GROUP BY t.TRIP_ID, t.TRIP_NAME
        ORDER BY t.TRIP_ID;
    """)
    run_query(conn, sql, title="Trips with Assigned Guides")

def report_trip_participants_count(conn):
    sql = dedent("""
        SELECT t.TRIP_ID,
               t.TRIP_NAME,
               IFNULL(SUM(r.NUM_PERSONS), 0) AS TotalParticipants
        FROM TRIP t
        LEFT JOIN RESERVATION r ON r.TRIP_ID = t.TRIP_ID
        GROUP BY t.TRIP_ID, t.TRIP_NAME
        ORDER BY TotalParticipants DESC, t.TRIP_ID;
    """)
    run_query(conn, sql, title="Trips Ranked by Total Participants")

def report_customer_total_spent(conn):
    sql = dedent("""
        SELECT c.CUSTOMER_NUM,
               c.LAST_NAME || ', ' || c.FIRST_NAME AS Customer,
               IFNULL(SUM(r.NUM_PERSONS * r.TRIP_PRICE + r.OTHER_FEES), 0) AS TotalSpent
        FROM CUSTOMER c
        LEFT JOIN RESERVATION r ON r.CUSTOMER_NUM = c.CUSTOMER_NUM
        GROUP BY c.CUSTOMER_NUM, Customer
        ORDER BY TotalSpent DESC;
    """)
    run_query(conn, sql, title="Customer Total Spent")

def report_trip_schema_like_figure(conn):
    sql = "PRAGMA table_info(TRIP);"
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    headers = ["Column", "Type", "NotNull", "PK"]
    formatted = []
    for cid, name, ctype, notnull, dflt_value, pk in rows:
        formatted.append((name, ctype, "No" if not notnull else "Yes", "Yes" if pk else "No"))
    print("\n=== PRAGMA table_info(TRIP) (Schema Overview) ===")
    print_table(headers, formatted)

def menu():
    print(dedent("""
        ============================
        Colonial DB - Python Console
        ============================
        1) Show GUIDE
        2) Show CUSTOMER
        3) Show TRIP
        4) Show RESERVATION
        5) Show TRIP_GUIDES
        6) REPORT: Reservation details (trip & customer)
        7) REPORT: Trips with assigned guides
        8) REPORT: Trips ranked by total participants
        9) REPORT: Customer total spent
        10) Show TRIP schema (like the figure)
        0) Exit
    """))

def main():
    if not os.path.exists(DB_PATH):
        print(f"ERROR: DB file not found.\n{DB_PATH}")
        return
    conn = sqlite3.connect(DB_PATH)
    while True:
        menu()
        choice = input("Choose: ").strip()
        if choice == "1":
            show_guide(conn)
        elif choice == "2":
            show_customer(conn)
        elif choice == "3":
            show_trip(conn)
        elif choice == "4":
            show_reservation(conn)
        elif choice == "5":
            show_trip_guides(conn)
        elif choice == "6":
            report_reservations_with_customer_and_trip(conn)
        elif choice == "7":
            report_trip_with_guides(conn)
        elif choice == "8":
            report_trip_participants_count(conn)
        elif choice == "9":
            report_customer_total_spent(conn)
        elif choice == "10":
            report_trip_schema_like_figure(conn)
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")
    conn.close()

if __name__ == "__main__":
    main()
