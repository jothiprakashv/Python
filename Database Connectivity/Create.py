import cx_Oracle
con=cx_Oracle.connect("admin/admin@XE")

cur=con.cursor()
cur.execute("""create table myemployee(
    empid number,
    empname varchar2(20),
    dept varchar2(20),
    designation varchar2(20),
    salary Number(7,2))""")

con.close()