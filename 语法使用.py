while True:
    d={1:'hello',2:'world',3:'fine',4:'hahha'}
    e=input('请输入一个键：')
    e=eval(e)
    print(d.get(e,'输入的健不存在！！！'))