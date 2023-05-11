# 随机生成密码
import random
import string
characters = string.ascii_letters + string.digits + string.punctuation
password = ''
for i in range(15):
    password += random.choice(characters)
print(password)
