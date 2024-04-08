'''Given an array of integers your solution should find the smallest integer.'''

def find_smallest_int(arr):
    smallest_int = arr[0]
    for i in arr:
        if smallest_int > i:
            smallest_int = i
    return smallest_int


'''Write a function that removes the spaces from the string, then return the resultant string.'''

def no_space(x):
    word = ""
    for c in x:
        if c != " ":
            word = word + c
    return word


'''Implement a function which convert the given boolean value into its string representation.'''

def boolean_to_string(b):
    if b == True:
        return "True"
    else:
        return "False"


'''Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then 
you should return 0.'''

def sum_array(a):
    sum = 0
    for v in a:
        sum += v
    return sum


print(18238*2)