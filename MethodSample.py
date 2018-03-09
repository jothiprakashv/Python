class MyClass:
    def __method(self):
        return 'instance method called', self

    def method1(self):
        return self.__method()

    @classmethod
    def method2(cls):
        return 'class method called', cls

    @staticmethod
    def method3():
        return 'static method called'


m=MyClass()
print(m.method1())
print(MyClass.method2())
print(MyClass.method3())
