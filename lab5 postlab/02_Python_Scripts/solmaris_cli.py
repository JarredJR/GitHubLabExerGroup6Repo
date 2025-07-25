import sqlite3
import os
from textwrap import dedent

DB_PATH = r"C:\Users\User\Desktop\Repository\Lab 5 PostLab\04_DB\sqlite\solmaris.db"

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

def show_location(conn):
    run_query(conn, "SELECT * FROM LOCATION ORDER BY LOCATION_ID;", title="LOCATION")

def show_condo_unit(conn):
    run_query(conn, "SELECT * FROM CONDO_UNIT ORDER BY UNIT_ID;", title="CONDO_UNIT")

def show_owner(conn):
    run_query(conn, "SELECT * FROM OWNER ORDER BY OWNER_ID;", title="OWNER")

def show_service_category(conn):
    run_query(conn, "SELECT * FROM SERVICE_CATEGORY ORDER BY CATEGORY_ID;", title="SERVICE_CATEGORY")

def show_service_request(conn):
    run_query(conn, "SELECT * FROM SERVICE_REQUEST ORDER BY REQUEST_ID;", title="SERVICE_REQUEST")

def report_requests_with_details(conn):
    sql = dedent("""
        SELECT sr.REQUEST_ID,
               sr.UNIT_ID,
               cu.UNIT_NO,
               l.LOCATION_NAME,
               sr.CATEGORY_ID,
               sc.CATEGORY_NAME,
               sc.DESCRIPTION,
               sr.STATUS,
               sr.REQUEST_DATE
        FROM SERVICE_REQUEST sr
        JOIN CONDO_UNIT cu     ON cu.UNIT_ID = sr.UNIT_ID
        JOIN LOCATION l        ON l.LOCATION_ID = cu.LOCATION_ID
        JOIN SERVICE_CATEGORY sc ON sc.CATEGORY_ID = sr.CATEGORY_ID
        ORDER BY sr.REQUEST_ID;
    """)
    run_query(conn, sql, title="Service Requests with Details")

def report_units_per_location(conn):
    sql = dedent("""
        SELECT l.LOCATION_ID,
               l.LOCATION_NAME,
               COUNT(cu.UNIT_ID) AS UnitCount
        FROM LOCATION l
        LEFT JOIN CONDO_UNIT cu ON cu.LOCATION_ID = l.LOCATION_ID
        GROUP BY l.LOCATION_ID, l.LOCATION_NAME
        ORDER BY l.LOCATION_ID;
    """)
    run_query(conn, sql, title="Units per Location")

def report_owner_units(conn):
    sql = dedent("""
        SELECT o.OWNER_ID,
               o.LAST_NAME || ', ' || o.FIRST_NAME AS OwnerName,
               COUNT(cu.UNIT_ID) AS NumUnits
        FROM OWNER o
        LEFT JOIN CONDO_UNIT cu ON cu.UNIT_ID = o.OWNER_ID
        GROUP BY o.OWNER_ID, OwnerName
        ORDER BY NumUnits DESC, o.OWNER_ID;
    """)
    run_query(conn, sql, title="Owner Units Count")

def report_category_request_counts(conn):
    sql = dedent("""
        SELECT sc.CATEGORY_ID,
               sc.CATEGORY_NAME,
               sc.DESCRIPTION,
               COUNT(sr.REQUEST_ID) AS RequestCount
        FROM SERVICE_CATEGORY sc
        LEFT JOIN SERVICE_REQUEST sr ON sr.CATEGORY_ID = sc.CATEGORY_ID
        GROUP BY sc.CATEGORY_ID, sc.CATEGORY_NAME, sc.DESCRIPTION
        ORDER BY RequestCount DESC, sc.CATEGORY_ID;
    """)
    run_query(conn, sql, title="Service Request Counts by Category")

def menu():
    print(dedent("""
        =========================
        Solmaris DB - Python Menu
        =========================
        1) Show LOCATION
        2) Show CONDO_UNIT
        3) Show OWNER
        4) Show SERVICE_CATEGORY
        5) Show SERVICE_REQUEST
        6) REPORT: Service Requests with details
        7) REPORT: Units per Location
        8) REPORT: Owner Units Count
        9) REPORT: Service Request Counts by Category
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
            show_location(conn)
        elif choice == "2":
            show_condo_unit(conn)
        elif choice == "3":
            show_owner(conn)
        elif choice == "4":
            show_service_category(conn)
        elif choice == "5":
            show_service_request(conn)
        elif choice == "6":
            report_requests_with_details(conn)
        elif choice == "7":
            report_units_per_location(conn)
        elif choice == "8":
            report_owner_units(conn)
        elif choice == "9":
            report_category_request_counts(conn)
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")
    conn.close()

if __name__ == "__main__":
    main()
