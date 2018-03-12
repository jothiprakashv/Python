import pickle

class Dog:
    
    def __init__(self,name,breed):
        self.__name=name
        self.__breed=breed

    def getName(self):
        return self.__name
    
    def getBreed(self):
        return self.__breed
    
    def walk(self):
        print("I can Walk")
    
    def bark(self):
        print("WOOF!")
    
jimmy = Dog("Jimmy","Labrador")
pickle.dump(jimmy,open("dogfile","wb"))

myDog=pickle.load(open("dogfile","rb"))
print(myDog.getName())
print(myDog.getBreed())
myDog.walk()
myDog.bark()
