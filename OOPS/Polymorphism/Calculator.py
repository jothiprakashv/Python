
class Calculator:
 
    # Overloaded __init__ method
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
 
    def add(self):
        return self.__x + self.__y
 
  
c1 = Calculator()
print(c1.add())

c1 = Calculator(2)
print(c1.add())

c1 = Calculator(2,5)
print(c1.add())
 

 
