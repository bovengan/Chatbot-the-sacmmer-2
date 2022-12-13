import sqlite3

sqliteConnection = sqlite3.connect('chatbot.db')
cursor = sqliteConnection.cursor()
cursor.execute("SELECT * FROM Users")
print(cursor.fetchall())
sqliteConnection.commit()
sqliteConnection.close()