import _sqlite3

pathToDB = "/Users/pratik.joshi/Documents/Projects/Python/sample.db"
connection = _sqlite3.connect(pathToDB)
cursor = connection.cursor()
x = 'john@email.com', 'John', 'Doe',
y = 'jane@email.com', 'Jane', 'Doe',
cursor.execute('INSERT INTO users VALUES (?,?,?)', x)
cursor.execute('INSERT INTO users VALUES (?,?,?)', y)
connection.commit()
connection.close()
print(cursor.rowcount)
