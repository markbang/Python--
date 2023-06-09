class Person:
    counter = 0

    def __init__(self,name,sex,age,fight_value):
        self.name = name
        self.sex = sex
        self.age = age
        self.fight_value = fight_value
        self.count()

    def eat(self):
        print(self.name+"正在吃饭")
        self.fight_value+=80

    def practice(self):
        print(self.name+"正在练功")
        self.fight_value+=200

    def battle(self):
        print(self.name+"正在打架")
        self.fight_value-=100

    # 计数玩家顺序
    def count(self):
        Person.counter+=1
        self.counter = Person.counter

    def info(self):
        print(f'I am player {self.counter} {self.name},I have {self.fight_value} fight_value')


xiaohua = Person("xiaohua","女",18,2000)
xiaoqian = Person("xiaoqian","男",19,1500)
xiaohua.eat()
xiaohua.practice()
xiaohua.info()
xiaoqian.info()