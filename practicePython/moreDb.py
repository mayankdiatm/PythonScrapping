import sqlite3


empList=((1,"arun",100),
         (2,"basu",200),
         (3,"chet",300),
         (4,"dine",400),
         (5,"elan",500)
        )
try:
  con = sqlite3.connect("test.db")  # connection
  cur = con.cursor()                # create cursor
  cur.execute('''create table emps( code integer,
                                  name character(10),
                                  salary integer)''')
  for e in empList:
   cur.execute("insert into emps values(?,?,?)",(e[0],e[1],e[2]))

  for i in cur.execute("select * from emps"):
   print(i)

  con.commit()                      # commit
except Exception as e:
  print(e)
finally:
  con.close()
