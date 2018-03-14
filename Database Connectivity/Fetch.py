import cx_Oracle

con=cx_Oracle.connect("admin/admin@XE")

cur=con.cursor()

cur.execute("select * from myemployee order by empid")

# row count
print(cur.rowcount)

# fetch all the records
print(cur.fetchall())

print(cur.rowcount)

cur.execute("select * from customerdetails order by custid")
# row count
print(cur.arraysize)

cur.arraysize=3

# fetch specified no. of records
print(cur.fetchmany())

con.commit()

con.close()