class Dog(object):
    counter = 0

    def __init__(self,name):
        self.name = name
        Dog.counter +=1

    def greet(self):
        print('Hello, I am {}{}'.format(self.name,self.counter))


class BarkingDog(Dog):
    def greet(self):
        print('Wolf! I am {}{}'.format(self.name,Dog.counter))


if __name__ == '__main__':
    dog = BarkingDog('hui')
    dog.greet()
