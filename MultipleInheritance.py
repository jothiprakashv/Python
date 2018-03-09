class Person():
    def __init__(self,name,age,gender,address,phone):
        self.__name=name
        self.__age=age
        self.__gender=gender
        self.__address=address
        self.__phone=phone

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


