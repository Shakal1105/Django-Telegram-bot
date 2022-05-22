import sqlite3

try:
        sqlite_connection = sqlite3.connect('db.sqlite3')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        records = cursor.objects.fetchall()
        print(records)
        for row in records:
            print("ID:", row[0])
            print("Имя:", row[1])
            print("Почта:", row[2])
            print("Добавлен:", row[3])
            print("Зарплата:", row[4], end="\n\n")

        cursor.close()

except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
