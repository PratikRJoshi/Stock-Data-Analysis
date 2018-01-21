import _sqlite3

pathToDB = "/Users/pratik.joshi/Documents/Projects/Python/sample.db"
connection = _sqlite3.connect(pathToDB)
cursor = connection.cursor()
x = 'Johnny', 'john@email.com',
cursor.execute('UPDATE users SET first = ? WHERE email = ?', x)
connection.commit()
connection.close()
print(cursor.rowcount)
