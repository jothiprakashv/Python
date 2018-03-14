import cx_Oracle


class Customer:

    def __init__(self, custId, name, age, address, phone):
        self.__custId = custId
        self.__name = name
        self.__age = age
        self.__address = address
        self.__phone = phone

    def getCustId(self):
        return self.__custId

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getAddress(self):
        return self.__address

    def getPhone(self):
        return self.__phone


c1 = Customer(5001, 'Raj Kumar', 20, 'Coimbatore', 9685321475)
c2 = Customer(5002, 'Allie', 25, 'Chennai', 9632568741)
c3 = Customer(5003, 'John Smith', 24, 'Trichy', 8695321457)
c4 = Customer(5004, 'Gopi', 22, 'Tirunelveli', 8896532147)

con = cx_Oracle.connect("admin/admin@XE")
cur = con.cursor()

""" Table creation script

create table customerdetails(
    custId number Primary Key,
    custname varchar2(25),
    age number(2),
    address varchar2(30),
    phone number(10));
"""

for customer in [c1, c2, c3, c4]:

    bindVar={'custId':customer.getCustId(),'custname':customer.getName(),'age':customer.getAge(),'address':customer.getAddress(),'phone':customer.getPhone()}

    cur.execute("""insert into customerdetails values(:custId,:custname,:age,:address,:phone)""", bindVar)


con.commit()
con.close()
