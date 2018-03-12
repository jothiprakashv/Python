from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    def __init__(self,model,no_of_wheels):
        self.__model=model
        self.__no_of_wheels=no_of_wheels

    def getModel(self):
        return self.__model

    def getNoOfWheels(self):
        return self.__no_of_wheels
    
    @abstractmethod
    def engine(self):
        return 

class Car(Vehicle):

    def __init__(self,model,no_of_wheels):
        super().__init__(model,no_of_wheels)

    def engine(self):
        return "4 stroke Engine"
    
    def __str__(self):
        return f"Car Model:{self.getModel()}\nWheels:{self.getNoOfWheels()}"

class Bike(Vehicle):

    def __init__(self,model,no_of_wheels):
        super().__init__(model,no_of_wheels)

    def engine(self):
        return "2 stroke Engine"
    
    def __str__(self):
        return f"Bike Model:{self.getModel()}\nWheels:{self.getNoOfWheels()}"


honda=Car("honda city",4)
print(honda)
print(honda.engine())

intruder=Bike("suzuki",2)
print(intruder)
print(intruder.engine())

#v = Vehicle("mymodel",5)
