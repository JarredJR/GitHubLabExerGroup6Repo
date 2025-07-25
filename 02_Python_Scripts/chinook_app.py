import sqlite3

def connect_db():
    return sqlite3.connect('../chinook.db')

def list_artists(limit=10):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT Name FROM artists LIMIT ?;", (limit,))
    rows = cursor.fetchall()
    print("\nTop Artists:")
    for row in rows:
        print("-", row[0])
    conn.close()

def main():
    while True:
        print("\n=== Chinook Database Menu ===")
        print("1. List Artists")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            list_artists()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
