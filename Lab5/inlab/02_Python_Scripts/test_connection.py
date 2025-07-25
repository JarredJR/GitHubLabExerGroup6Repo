import sqlite3

try:

    conn = sqlite3.connect('../chinook.db') 
    cursor = conn.cursor()


    cursor.execute("SELECT Name FROM artists LIMIT 5;")
    artists = cursor.fetchall()

    print("Successfully connected to chinook.db")
    print("Here are 5 artists:")
    for artist in artists:
        print("-", artist[0])

except Exception as e:
    print("Error:", e)
finally:
    if conn:
        conn.close()
