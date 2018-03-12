import cx_Oracle
con=cx_Oracle.connect("admin/admin@XE")
print(con.version)
con.close()