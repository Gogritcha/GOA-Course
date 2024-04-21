# '''Implement a function that accepts 3 integer values a, b, c. 
# The function should return true if a triangle can be built with the sides of given length and false in any other case.'''

# def is_triangle(a, b, c):
#     if c < a + b and a < c + b and b < a + c:
#         return True
#     else:
#         return False
    

def capitals(word):
    b = []
    a = []
    for i in word:
        a.append(i)
        if i.isupper:
            b.append(len(a)-1)
    return b


print(capitals("CodEWaRs"))