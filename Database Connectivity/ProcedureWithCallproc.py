import cx_Oracle
try:
    con=cx_Oracle.connect("admin/admin@XE")
    con.begin()
    cur=con.cursor()

    #stored procedure to retrieve the number of employees 
    #belonging to a particular department

    cur.execute(""" CREATE or REPLACE PROCEDURE sp_checkemplyoee_Dept (deptName IN myemployee.dept%Type, d_out OUT NUMBER)
    AS
    d_count number;
    BEGIN
    select count(*) into d_count from myemployee where dept=deptName;
    if(d_count=0) then
        d_out:=0;
        return;
    end if;
    d_out:=d_count;
    return;
    END;
    """)

    #declare output variable
    myResult=cur.var(cx_Oracle.NUMBER)
    dept='Finance'

    #invoke the stored procedure
    cur.callproc('sp_checkemplyoee_Dept',[dept,myResult])
    no_of_employees=myResult.getvalue()
   
    if(no_of_employees==0):
        print(f"No employee exist in {dept}")
    else:
        print(f"{no_of_employees} employee(s) exist in {dept}")

except cx_Oracle.Error as e:
    print(e)
    con.rollback()
finally:
    con.commit()
    con.close()