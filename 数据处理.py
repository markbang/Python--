#  读入name.txt文件中的内容，,即将敏感词汇和谐一下，多添加一些敏感词汇，比如暴力-和平，恐怖-美好，等等,只是把敏感词汇替换，不改变原文件其他内容
with open('name.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    print(text)
    text = text.replace('暴力', '和平')
    text = text.replace('恐怖', '美好')
    print(text)
