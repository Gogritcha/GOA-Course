'''Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. 
No floats or non-positive integers will be passed.'''

def sum_two_smallest_numbers(num_list):
    b = []
    c = 0
    for i in num_list:
        if i != min(num_list):
            b.append(i)
        else:
            c += min(num_list)
    for i in b:
        if i == min(b):
            c += min(b)
    return c


'''Make a program that filters a list of strings and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...'''

def friend(x):
    b = 0
    c = []
    for i in x:
        if len(i) == 4:
            c.append(i)
            b += 1
    return c


'''You are going to be given a word. Your job is to return the middle character of the word. 
If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.'''

def get_middle(s):
    if len(s) % 2 == 0 and len(s):
        return str(s[int(len(s)/2-1)]+s[int(len(s)/2)])
    if len(s) % 2 != 0:
        return s[int(len(s)/2-0.5)]


