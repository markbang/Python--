txt = 'If the implementation is eAsy to exPLAin, it may be a good idea.'


def bianxiao(text):
    for index, char in enumerate(text):
        if text[index-1].isalpha() and char.isupper() and text[index+1].isalpha():
            text = text.replace(char, char.lower())
    return text


print(bianxiao(txt))