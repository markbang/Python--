def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
def chat():
    print('我是函数')
def happyA(name):
    print('Happy Birthday Dear {}'.format(name))
def max(a,b):
    if a>b:
        result=a
    else:
        result=b
    return result
def fib(n):
    a,b=1,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
    print()
def vfunc(a,*b):
    print(type(b))
    for n in b:
        a+=n
    return a
def jiecheng(n,*b):
    s=1
    for i in range(1,n+1):
        s*=i
    for item in b:
        s*=item
    return s
f=lambda x,y:x+y
print(f(10,12))
