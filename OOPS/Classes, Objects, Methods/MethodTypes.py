class MethodTypes:

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


m=MethodTypes()
print(m.method1())
print(MethodTypes.method2())
print(MethodTypes.method3())
