class Person():

    def __init__(self,name,age,gender,address,phone):
        self.__name=name
        self.__age=age
        self.__gender=gender
        self.__address=address
        self.__phone=phone

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getGender(self):
        return self.__gender

    def getAddress(self):
        return self.__address 

    def getPhone(self):
        return self.__phone

    def speak(self):
        return "I can speak"

    def walk(self):
        return "I can walk" 

class Employee():

    def __init__(self,empid,dept,doj,designation,salary):
        self.__empid=empid
        self.__dept=dept
        self.__doj=doj
        self.__designation=designation
        self.__salary=salary

    def getEmpid(self):
        return self.__empid
    
    def getDept(self):
        return self.__dept
    
    def getDoj(self):
        return self.__doj
    
    def getDesignation(self):
        return self.__designation
    
    def getSalary(self):
        return self.__salary

    def work(self):
        return f"I am working as {self.getDesignation()} in {self.getDept()} since {self.getDoj()}"

class Teacher(Person,Employee):

    def __init__(self,name,age,gender,address,phone,empid,dept,doj,designation,salary,course_Handling,isTutor):
        Person.__init__(self,name,age,gender,address,phone)
        Employee.__init__(self,empid,dept,doj,designation,salary)
        self.__course_Handling = course_Handling
        self.__isTutor = isTutor

    def __str__(self):
        return f"Teacher Details\nName={self.getName()}\nAge={self.getAge()}\nGender={self.getGender()}\nAddress={self.getAddress()}\nPhone={self.getPhone()}\nEmployee Id={self.getEmpid()}\nDepartment={self.getDept()}\nDate of Joining={self.getDoj()}\nDesignation={self.getDesignation()}\nSalary=Rs.{self.getSalary()}\nCourse={self.__course_Handling}\nisTutor={self.__isTutor}"


kumar=Teacher("Kumar",27,"Male","Coimbatore",9876543255,"EM1001","IT","05/05/2014","Assistant Professor","27000","Python","No")
print(kumar)
print(kumar.speak())
print(kumar.walk())
print(kumar.work())
