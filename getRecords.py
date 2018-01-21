import _sqlite3

pathToDB = "/Users/pratik.joshi/Documents/Projects/Python/sample.db"
connection = _sqlite3.connect(pathToDB)
cursor = connection.cursor()
x = 'kirk', 'Chan',
cursor.execute('Select email, first, last from users WHERE last = ? OR last = ?', x)
for row in cursor.fetchall():
    print(row[0], row[1], row[2])
cursor.execute('Select * from users')
for row in cursor.fetchall():
    print(row)
connection.close()
