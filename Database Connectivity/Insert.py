import cx_Oracle
con=cx_Oracle.connect("admin/admin@XE")

cur=con.cursor()

cur.execute("""insert into myemployee values(1001,'Ramesh','Accounts','Manager','50250.00')""")

con.commit()

con.close()