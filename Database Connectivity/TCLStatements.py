import cx_Oracle
con=cx_Oracle.connect("admin/admin@XE")
con.begin()
cur=con.cursor()

cur.execute("""insert into myemployee values(1007,'Ragav','Finance','Clerk',25236.00)""")
cur.execute("""savepoint s1""")

cur.execute("""insert into myemployee values(1008,'Guru','Finance','Clerk',20053.00)""")
cur.execute("""savepoint s2""")

cur.execute("""insert into myemployee values(1009,'Michael','Accounts','Clerk',21456.00)""")
cur.execute("""savepoint s3""")

cur.execute("select * from myemployee order by empid")
print(cur.fetchall())

cur.execute("""rollback to s2""")

cur.execute("select * from myemployee order by empid")
print(cur.fetchall())

cur.execute("""rollback to s1""")

cur.execute("select * from myemployee order by empid")
print(cur.fetchall())

con.commit()

con.close()