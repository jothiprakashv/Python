import cx_Oracle
con=cx_Oracle.connect("admin/admin@XE")

cur=con.cursor()

cur.execute("""delete from myemployee where empid=:1""",(1001,))

con.commit()

con.close()