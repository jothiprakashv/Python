class AccessSpecifiers:

    def __init__(self,name,email,age):
        self.name=name      # public
        self._email=email   # protected
        self.__age=age      # private
    
myObj=AccessSpecifiers("Kevin","kevin@minions.com",12)
print(myObj.name)
print(myObj._email)
print(myObj.age)
