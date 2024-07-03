def invert(lst):
    result = []
    if lst != []:
        for i in lst:
            if i > 0:
                result.append(-i)
            elif i < 0:
                result.append(abs(i))
            else:
                result.append(i)
        return result
    else:
        return lst
    

def smash(words):
    if len(words) > 1:
        a = " ".join(words)
        return a
    elif words == []:
        return ""
    else:
        return words[0]


def between(a,b):
    result = []
    for i in range(a,b+1):
        result.append(i)
    return result


def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3
    if average >= 90:
        return "A"
    elif average >= 80 and average < 90:
        return "B"
    elif average >= 70 and average < 80:
        return "C"
    elif average >= 60 and average < 70:
        return "D"
    else:
        return "F"


def dna_to_rna(dna):
    rna = ""
    for i in dna:
        if i == "T":
            rna += "U"
        else:
            rna += i
    return rna


def stray(arr):
    if arr[0] == arr[1]:
        for i in arr:
            if i != arr[0]:
                return i
    else:
        if arr[0] != arr[2]:
            return arr[0]
        else:
            return arr[1]


def round_to_next5(n):
    if n % 5 != 0:
        while n % 5 != 0:
            n += 1
        return n
    else:
        return n


def spot_diff(s1, s2):
    result = []
    x = 0
    if s1 != s2:
        for i in s1:
            if i != s2[x]:
                result.append(len(s2[:x]))
            x += 1
        return result
    else:
        return []


def DNA_strand(dna):
    result = ""
    for i in dna:
        if i == "A":
            result += "T"
        elif i == "T":
            result += "A"
        elif i == "G":
            result += "C"
        else:
            result += "G"
    return result


def camel_case(s):
    a = s.split(" ")
    b = []
    for i in a:
        i = i.capitalize()
        b.append(i)
    return("".join(b))