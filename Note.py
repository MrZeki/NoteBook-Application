import sqlite3

conn = sqlite3.connect("C:/Users/zeki/PycharmProjects/NoteProject/List.db")
Cursor = conn.cursor()

Cursor.execute("""
CREATE TABLE IF NOT EXISTS note(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    notlar TEXT
)
""")

while True:
    print("\nWelcome To The Note Application")
    print("1-Add Note")
    print("2-List Notes")
    print("3-Search Notes by Word")
    print("4-Delete Note")
    print("5-Exit")

    P = input("What Would You Like To Do = ")

    if P == "1":
        note = input("Note = ")
        try:
            Cursor.execute("INSERT INTO note(notlar) VALUES (?)", (note,))
            conn.commit()
            print("Note added successfully")
        except Exception as e:
            print("Error:", e)

    elif P == "2":
        try:
            Cursor.execute("SELECT * FROM note")
            notes = Cursor.fetchall()
            for row in notes:
                print(row)
        except Exception as e:
            print("Error:", e)

    elif P == "3":
        w = input("Search word = ")
        try:
            Cursor.execute("SELECT * FROM note WHERE notlar LIKE ?", (f"%{w}%",))
            results = Cursor.fetchall()
            if results:
                for r in results:
                    print(r)
            else:
                print("No matching notes.")
        except Exception as e:
            print("Error:", e)

    elif P == "4":
        try:
            n = int(input("Enter id to delete = "))
            Cursor.execute("DELETE FROM note WHERE id = ?", (n,))
            conn.commit()
            print("Deleted")
        except Exception as e:
            print("Error:", e)

    elif P == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
