# 随机生成密码
import random
import string
characters = string.ascii_letters + string.digits + string.punctuation
pwd = ''
for i in range(15):
    pwd += random.choice(characters)
print(pwd)
# 判断密码强度


def check(password):
    if not isinstance(password, str):
        raise TypeError('password should be str')
    elif len(password) < 8:
        return 'weak'
    elif len(password) >= 8 and password.isalpha():
        return 'weak'
    elif len(password) >= 8 and password.isalnum():
        return 'medium'
    elif len(password) >= 8 and password.isalnum() and password.isupper():
        return 'strong'
    elif len(password) >= 8 and password.isalnum() and password.islower():
        return 'strong'
    elif len(password) >= 8 and password.isalnum() and password.isupper() and password.islower():
        return 'very strong'
    else:
        return 'truly strong'


print(check('123hahjiJK'))

