import _sqlite3

pathToDB = "/Users/pratik.joshi/Documents/Projects/Python/resources/sample.db"
connection = _sqlite3.connect(pathToDB)
cursor = connection.cursor()
x = 'john@email.com',
cursor.execute('DELETE FROM users WHERE email = ?', x)
connection.commit()
connection.close()
print(cursor.rowcount)
