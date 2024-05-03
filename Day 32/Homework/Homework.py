'''The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!'''

def generate_hashtag(s):
    j = "#"
    x = 0
    a = s.split(" ")
    for i in a:
        j += a[x].capitalize()
        x += 1
    if len(j) > 140 or s == "":
        return False
    return j


'''The variance for a set of numbers is found by subtracting the mean from every value, squaring the results, 
adding them all up and dividing by the number of elements.'''

def variance(numbers): 
    a = 0
    x = 0
    c = 0
    for b in numbers:
        c += b
    for i in numbers:
        i = (numbers[x]-c/len(numbers))**2
        a += i
        x += 1
    return a / len(numbers)