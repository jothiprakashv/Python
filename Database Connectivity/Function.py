import cx_Oracle
try:
    con=cx_Oracle.connect("admin/admin@XE")
    con.begin()
    cur=con.cursor()

    #stored function to retrieve all employees 
    cur.execute("""
    CREATE OR REPLACE FUNCTION fn_list_all return SYS_REFCURSOR
    AS
   
    listall SYS_REFCURSOR;
   
    BEGIN
    open listall for 
        select * from myemployee;
    return listall;

    END fn_list_all;
    """)

    #invoke the stored procedure
    my_cursor=cur.callfunc('fn_list_all',returnType=cx_Oracle.CURSOR)
    print("Employee Details")
    print('*'*20)
    for row in my_cursor:
        print(row)

except cx_Oracle.Error as e:
    print(e)
    con.rollback()
finally:
    con.commit()
    con.close()