'''Return the number (count) of vowels in the given string.'''

def get_count(sentence):
    len = 0
    for i in sentence:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            len += 1
    return len


'''Write function bmi that calculates body mass index (bmi = weight / height2).'''

def bmi(weight, height):
    bmi = weight/(height**2)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"


'''In this kata, you are asked to square every digit of a number and concatenate them.'''

def square_digits(num):
    a = ""
    for i in str(num):
        squared = int(i)**2
        a = a + str(squared)
    return int(a)


'''Given a non-empty array of integers, return the result of multiplying the values together in order. Example:'''

def grow(arr):
    a = 1
    for i in arr:
        a = a * i
    return a


'''Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0.'''

def solution(number):
    sum = 0
    if number > 0:
        for i in range(number-1,0,-1):
            if i % 3 == 0 or i % 5 == 0:
                sum += i
        return sum
    if number <= 0:
        return 0
    
