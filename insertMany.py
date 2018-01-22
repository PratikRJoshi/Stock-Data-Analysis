import _sqlite3

pathToDB = "/Users/pratik.joshi/Documents/Projects/Python/resources/sample.db"
connection = _sqlite3.connect(pathToDB)
cursor = connection.cursor()
employees = [('jill@mail.com', 'Jill', 'AppleTree'),
             ('frank@mail.com', 'Frank', 'AppleTree'),
             ('desi@mail.com', 'Desi', 'AppleTree'),]
cursor.executemany('INSERT INTO users VALUES (?,?,?)', employees)
connection.commit()
connection.close()
print(cursor.rowcount)