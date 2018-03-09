class Learner:
    def __init__(self):
        self.classes = []

    def enrol(self, course):
        self.classes.append(course)


class Teacher:
    def __init__(self,name):
        self.name=name
        self.courses_taught = ["C","C++","Java","Python"]

    def assign_teaching(self, course):
        self.courses_taught.append(course)


class Person:
    def __init__(self, name, surname, number, learner=None, teacher=None):
        self.name = name
        self.surname = surname
        self.number = number
        #Here the Person class Has-A learner and teacher as attributes
        self.learner = learner
        self.teacher = teacher
        
    def __str__(self):
        return f"Person Details:\nName:{self.name}\nEnrollment No:{self.number}\nCourses Enrolled:{self.learner.classes}\nTeacher:{self.teacher.name}"
        

myobj = Person("Raj", "Kumar", "SMTJNX045", Learner(), Teacher("John"))
myobj.learner.enrol("Python")
myobj.teacher.assign_teaching("Python")
print(myobj)
