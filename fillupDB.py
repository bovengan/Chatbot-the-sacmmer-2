import sqlite3

sqliteConnection = sqlite3.connect('chatbot.db')
cursor = sqliteConnection.cursor()
#rows = [('C0', 20, 'Richard',4,0,1,0,30,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)]
#rows = [('C1', 21, 'Noel',5,1,1,1,20,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0)]
cursor.executemany('INSERT INTO Users VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', rows)
sqliteConnection.commit()
sqliteConnection.close()