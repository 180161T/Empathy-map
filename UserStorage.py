import sqlite3
with sqlite3.connect("UserStorage.db") as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
username VARCHAR(20) NOT NULL ,
password VARCHAR(20) NOT NULL) ;
''')

cursor.execute('''
VALUES("Xavier","xlyx")
''')
db.commit()

cursor.execute("SELECT * FROM user")
cursor.fetchall()