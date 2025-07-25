import sqlite3
import os
from textwrap import dedent

DB_PATH = r"C:\Users\User\Desktop\Repository\Lab 5 PostLab\04_DB\sqlite\tal.db"

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

def show_rep(conn):
    run_query(conn, "SELECT * FROM REP ORDER BY REP_NUM;", title="REP")

def show_customer(conn):
    run_query(conn, "SELECT * FROM CUSTOMER ORDER BY CUSTOMER_NUM;", title="CUSTOMER")

def show_orders(conn):
    run_query(conn, "SELECT * FROM ORDERS ORDER BY ORDER_NUM;", title="ORDERS")

def show_item(conn):
    run_query(conn, "SELECT * FROM ITEM ORDER BY ITEM_NUM;", title="ITEM")

def show_order_line(conn):
    run_query(conn, "SELECT * FROM ORDER_LINE ORDER BY ORDER_NUM, ITEM_NUM;", title="ORDER_LINE")

def report_orders_with_customer(conn):
    sql = dedent("""
        SELECT o.ORDER_NUM,
               o.ORDER_DATE,
               o.CUSTOMER_NUM,
               c.CUSTOMER_NAME
        FROM ORDERS o
        JOIN CUSTOMER c ON c.CUSTOMER_NUM = o.CUSTOMER_NUM
        ORDER BY o.ORDER_DATE, o.ORDER_NUM;
    """)
    run_query(conn, sql, title="Orders with Customer Name")

def report_order_totals(conn):
    sql = dedent("""
        SELECT o.ORDER_NUM,
               o.ORDER_DATE,
               c.CUSTOMER_NAME,
               SUM(ol.NUM_ORDERED * ol.QUOTED_PRICE) AS OrderTotal
        FROM ORDERS o
        JOIN CUSTOMER c  ON c.CUSTOMER_NUM = o.CUSTOMER_NUM
        JOIN ORDER_LINE ol ON ol.ORDER_NUM = o.ORDER_NUM
        GROUP BY o.ORDER_NUM, o.ORDER_DATE, c.CUSTOMER_NAME
        ORDER BY o.ORDER_DATE, o.ORDER_NUM;
    """)
    run_query(conn, sql, title="Order Totals")

def report_customer_balance_vs_credit(conn):
    sql = dedent("""
        SELECT CUSTOMER_NUM,
               CUSTOMER_NAME,
               BALANCE,
               CREDIT_LIMIT,
               (CREDIT_LIMIT - BALANCE) AS RemainingCredit
        FROM CUSTOMER
        ORDER BY RemainingCredit ASC;
    """)
    run_query(conn, sql, title="Customer Balance vs Credit Limit")

def report_rep_sales_totals(conn):
    sql = dedent("""
        SELECT r.REP_NUM,
               r.LAST_NAME || ', ' || r.FIRST_NAME AS RepName,
               IFNULL(SUM(ol.NUM_ORDERED * ol.QUOTED_PRICE), 0) AS TotalSales
        FROM REP r
        LEFT JOIN CUSTOMER c ON c.REP_NUM = r.REP_NUM
        LEFT JOIN ORDERS o    ON o.CUSTOMER_NUM = c.CUSTOMER_NUM
        LEFT JOIN ORDER_LINE ol ON ol.ORDER_NUM = o.ORDER_NUM
        GROUP BY r.REP_NUM, RepName
        ORDER BY TotalSales DESC;
    """)
    run_query(conn, sql, title="Rep Sales Totals")

def menu():
    print(dedent("""
        =====================
        TAL DB - Python Menu
        =====================
        1) Show REP
        2) Show CUSTOMER
        3) Show ORDERS
        4) Show ITEM
        5) Show ORDER_LINE
        6) REPORT: Orders with Customer Name
        7) REPORT: Order Totals
        8) REPORT: Customer Balance vs Credit Limit
        9) REPORT: Rep Sales Totals
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
            show_rep(conn)
        elif choice == "2":
            show_customer(conn)
        elif choice == "3":
            show_orders(conn)
        elif choice == "4":
            show_item(conn)
        elif choice == "5":
            show_order_line(conn)
        elif choice == "6":
            report_orders_with_customer(conn)
        elif choice == "7":
            report_order_totals(conn)
        elif choice == "8":
            report_customer_balance_vs_credit(conn)
        elif choice == "9":
            report_rep_sales_totals(conn)
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")
    conn.close()

if __name__ == "__main__":
    main()
