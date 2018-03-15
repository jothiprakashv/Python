import cx_Oracle
try:
    con=cx_Oracle.connect("admin/admin@XE")
    con.begin()
    cur=con.cursor()

    #stored procedure to retrieve the number of employees 
    #belonging to a particular department

    cur.execute(""" CREATE or REPLACE PROCEDURE myemployee_raise_sal (id IN myemployee.empid%Type, percent IN NUMBER, s_out OUT NUMBER)
    AS
    BEGIN
    update myemployee set salary=salary+salary *(percent/100) where empid=id;
    commit;
    select salary into s_out from myemployee where empid=id;
    return;
    END;
    """)

    # calling procedure myemployee_raise_sal
    out_parameter = cur.var(cx_Oracle.STRING)
    empId=1002
    # we can enclose procedure call between BEGIN and END
    # The BEGIN/END is not required but recommended for clarity.
    plsql = "BEGIN myemployee_raise_sal(:empid, :percent, :out); END;"
    execute_proc = cur.execute(plsql, (empId, 10, out_parameter))
 
    print (f"updated salary for {empId} is Rs. {out_parameter.getvalue()}")

except cx_Oracle.Error as e:
    print(e)
    con.rollback()
finally:
    con.commit()
    con.close()