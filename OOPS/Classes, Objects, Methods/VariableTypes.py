class VariableTypes:

    # class variable
    counter=0 
    
    def __init__(self):
        # instance variable
        self.name="John" 
        VariableTypes.counter += 1       

myObj1=VariableTypes()
print(myObj1.name)
print(myObj1.counter)

myObj2=VariableTypes()
print(myObj2.name)
print(myObj2.counter)

print(myObj1.counter)

