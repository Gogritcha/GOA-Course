'''https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python'''

def duplicate_encode(word):
    word = word.lower()
    c = 0
    result = ""
    for i in word:
        if word.count(i) > 1:
            result += ")"
        else:
            result += "("
    return result