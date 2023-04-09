import sqlite3

connect = sqlite3.connect('shop.db')
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS catagory(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
name VARCHAR(50) NOT NULL,
describe TEXT
)
''') #crud

# cursor.execute('''
# INSERT INTO catagory(name, describe) VALUES("LAPTOPS", "Найлучшие ноутбуки!")
# ''')
connect.commit()
cursor.execute('SELECT * FROM catagory')

catagorys = cursor.fetchall()

print(catagorys)
cursor.close()
connect.close()