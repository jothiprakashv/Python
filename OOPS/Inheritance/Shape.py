class Shape():
    def __init__(self,x=0,y=0):
        self.__x=x
        self.__y=y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def area(self):
        print("undefined")

class Rectangle(Shape):
    def __init__(self,x,y):
        super().__init__(x,y)

    def area(self):
        return "Area of Rectangle is:"+str(self.getX() * self.getY())

class Triangle(Shape):
    def __init__(self,x,y):
        super().__init__(x,y)

    def area(self):
        return "Area of Triangle is:"+str(super().getX() * super().getY()* 0.5)

class Cube(Shape):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.__z=z
        
    def area(self):
        return "Area of Cube is:"+str(super().getX() * super().getY()* self.__z)

s=Shape()

print(isinstance(s,Shape))
print(isinstance(s,Rectangle))
print(isinstance(s,Triangle))
print(isinstance(s,Cube))

r=Rectangle(4,5)
s=r
print(s.area())

#checking if 's' is an instance of class Rectangle (sub class) and Shape (super class)
print(isinstance(s,Rectangle))
print(isinstance(s,Shape))

#checking if the Rectangle is subclass of Shape
print(issubclass(Rectangle,Shape))

t=Triangle(4,3)
s=t
print(s.area())
print(isinstance(s,Triangle))
print(isinstance(s,Shape))
print(issubclass(Triangle,Shape))

c=Cube(2,3,4)
s=c
print(s.area())
print(isinstance(s,Cube))
print(isinstance(s,Shape))
print(issubclass(Cube,Shape))

