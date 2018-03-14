import cx_Oracle
con=cx_Oracle.connect("admin/admin@XE")

cur=con.cursor()

employees=[ (1002,"Gopi","Accounts","Assistant",12500.00),(1003,"James","Finance","Manager",45275.00),(1004,"Hitler","Finance","Cashier",30500.00),(1005,"Lenin","Accounts","Assistant",12500.00)]

cur.executemany("""insert into myemployee values(:1,:2,:3,:4,:5)""",employees)

con.commit()

con.close()