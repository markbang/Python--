class Test:
    def __init__(self,value):
        self.__value = value

    def __get(self):
        return self.__value

    def __set(self,value):
        self.__value = value

    def __del(self):
        del self.__value

    value = property(__get,__set,__del)

    def show(self):
        print(self.__value)


t = Test(100)
t.value = 200
del t.value

