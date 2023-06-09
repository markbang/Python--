class BMI:
    data = 0

    def __init__(self,high,weight):
        self.high = high
        self.weight = weight
        BMI.data = self.weight/(self.high**2)

    def printBMI(self):
        print('你的BMI指数为：',self.weight/(self.high**2))


class ChinaBMI(BMI):
    def printBMI(self):
        if BMI.data > 18:
            print('正常', self.data)
        else:
            print('生病啦', self.data)


if __name__ == '__main__':
    high = float(input('请输入身高（单位m）'))
    weight = float(input('请输入体重（单位kg）'))
    xiaoming = ChinaBMI(high=high,weight=weight)
    xiaoming.printBMI()