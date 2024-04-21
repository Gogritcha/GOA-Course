'''Implement a function that accepts 3 integer values a, b, c. 
The function should return true if a triangle can be built with the sides of given length and false in any other case.'''

def is_triangle(a, b, c):
    if c < a + b and a < c + b and b < a + c:
        return True
    else:
        return False
    

'''Complete the solution so that the function will break up camel casing, using a space between words.'''

def solution(s):
    a = ""
    for i in s:
        if i.isupper():
            a += " "
        a += i
    return a


'''Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.'''

def is_prime(n):
    if n <= 1:
        return False
    c = 2
    while c <= n ** 0.5:
        if n % c == 0:
            return False
        c += 1
    return True


'''Write a function that when given a number >= 0, returns an Array of ascending length subarrays.'''

def pyramid(n):
    new_list = []
    for i in range(1, n + 1):
        new_list.append(i * [1])
    return new_list