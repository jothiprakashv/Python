import cx_Oracle
con=cx_Oracle.connect("admin/admin@XE")

cur=con.cursor()

cur.execute("""update myemployee set dept='{}' where empid={}""".format("Income Tax",1003))

con.commit()

con.close()