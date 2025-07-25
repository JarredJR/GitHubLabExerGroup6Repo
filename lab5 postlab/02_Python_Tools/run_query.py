import sqlite3, csv, sys, pathlib

def run_query(db_path, sql, out_csv=None):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    headers = [d[0] for d in cur.description] if cur.description else []
    if out_csv:
        with open(out_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if headers: writer.writerow(headers)
            writer.writerows(rows)
    else:
        print(headers)
        for r in rows:
            print(r)
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python run_query.py <db_path> <sql_file> [csv_out]")
        sys.exit(1)
    db = sys.argv[1]
    sql = pathlib.Path(sys.argv[2]).read_text(encoding='utf-8')
    out = sys.argv[3] if len(sys.argv) > 3 else None
    run_query(db, sql, out)
