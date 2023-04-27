d={}
for i in range(26):
    d[chr(i+ord('a'))]=chr((i+13)%26+ord('a'))
    print(d)
for c in 'Python':
    print(d.get(c,c),end='')