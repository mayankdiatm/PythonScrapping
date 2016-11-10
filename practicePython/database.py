import sqlite3

try:
    db = sqlite3.connect("test.db")
    cur = db.cursor()
    cur.execute('''create table products(
            name character(10),
            qty  integer)''')
    cur.execute("insert into products values ('a',10)")
    db.commit()
    for i in cur.execute("select * from products"):
      print("ROW = ",i)
except Exception as e:
    print(e)
finally:
    db.close()