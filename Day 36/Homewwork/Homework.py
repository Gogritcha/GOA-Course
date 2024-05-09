'''https://www.codewars.com/kata/520b9d2ad5c005041100000f 5 kyu'''

def pig_it(text):
    words = text.split()
    res = ""
    for word in words:
        res += word[1:]
        res += word[0]
        if word [-1] in ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]:
            res += "ay"
        res += " "
    res = res[:-1]
    return res


'''https://www.codewars.com/kata/529eef7a9194e0cbc1000255 7 kyu'''

def is_anagram(test, original):
    a = ""
    d = ""
    for i in test:
        b = i.lower()
        a += b
    for l in original:
        c = l.lower()
        d += c
    return sorted(a) == sorted(d)


'''https://www.codewars.com/kata/5500d54c2ebe0a8e8a0003fd'''

def mygcd(x, y):
    while y > 0:
        x, y = y, x % y
        
    return x


'''https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python'''

def expanded_form(num):
    num_str = str(num)
    expanded = []
    length = len(num_str)
    for i in range(length):
        digit = num_str[i]
        if digit != '0':
            expanded.append(digit + '0' * (length - i - 1))
    return ' + '.join(expanded)


'''https://www.codewars.com/kata/569d488d61b812a0f7000015'''

def data_reverse(data):
    a = ""
    x = 0
    o = []
    for i in data:
        a += str(i)
        x += 1
        if x == 8:
            x = 0
            a += " "
    v = a.split()
    v = v[::-1]
    v = ("").join(v)
    for t in v:
        o.append(int(t))
    return o


'''https://www.codewars.com/kata/57f8ff867a28db569e000c4a'''

def kebabize(st):
    a = ""
    x = 0
    for i in st:
        if i.isupper():
            if x > 0:
                a += "-"
            a += i.lower()
        elif i not in ["1","2","3","4","5","6","7","8","9","0"]:
            a += i 
        x += 1
    if a != "":
        if a[0] == "-":
            a = a[0:]
    return a


'''https://www.codewars.com/kata/5286b2e162056fd0cb000c20/train/python'''

def collatz(num):
    sequence = [num]
    while num >1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num *3 +1
        sequence.append(num)
    sequence = [str(x) for x in sequence]
    return "->".join(sequence)


'''https://www.codewars.com/kata/545cedaa9943f7fe7b000048'''

def is_pangram(s):
    a = ""
    v = ""
    x = 0
    for i in s:
        if i in ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]:
            a += i.lower()
    a = sorted(a)
    for t in a:
        if x == 1:
            if t != v[-1]:
                v += t
        if x != 1:
            v += t
            x += 1
    return v == "abcdefghijklmnopqrstuvwxyz"





def manual_reverse(word1):
    result = ""
    c = 0
    modified_word1 = word1
    while sorted(result) != sorted(word1):
        x = 0
        while x != len(modified_word1):
            for i in modified_word1:
                b = 0
            x += 1
        result += i
        modified_word1 = modified_word1[:-1]
    return result


def manual_replace(word2,replace_this,replace_with_this):
    a = ""
    for i in word2:
        if i == replace_this:
            i = replace_with_this
            a += i
        else:
            a += i
    return a


def manual_count(word3,counted_symbol):
    a = 0
    for i in word3:
        if i == counted_symbol:
            a += 1
    return a