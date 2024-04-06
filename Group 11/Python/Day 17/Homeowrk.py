'''Write a function that takes a list of numbers as input and returns the sum of all the numbers in the list.'''
def num_sum(nums):
    sum = 0
    for i in nums:
        sum += i
    return sum

nums= [4,5,65,7,2,67,8,9]

print(num_sum(nums))


'''Write a function that takes a list of strings as input and returns a new list containing only the strings that have a length greater than 5.'''
def words(wordz):
    words_grater_than_5 = []
    for a in wordz:
        if len(a) > 5:
            words_grater_than_5.append(a)
    return words_grater_than_5

wordz = ['sad','happy','Greatful']

print(words(wordz))


'''Write a function that takes a list of numbers as input and returns a new list containing only the even numbers from the original list.'''
def even_numbers(numbers_in_list):
    even_numberz = []
    for b in numbers_in_list:
        if b % 2 == 0:
            even_numberz.append(b)
    return even_numberz

numbers_in_list = [2,5,6,8,10,9,23]

print(even_numbers(numbers_in_list))
    

'''Write a function that takes a list of numbers as input and returns the largest number in the list.'''
def numbers(numberz):
    largest_number = max(numberz)
    return largest_number

numberz = [7,3,4,5,6,100,190]

print(numbers(numberz))


'''Write a function that takes a list of strings as input and returns a new list containing only the strings that start with the letter 'a'.'''
def sityvebi(sityvani):
    stiytvebi_romlebic_a_ti_iwyeba = []
    for c in sityvani:
        if c[0] == "a" or c[0] == "A":
            stiytvebi_romlebic_a_ti_iwyeba.append(c)
    return stiytvebi_romlebic_a_ti_iwyeba

sityvani = ["America","Georgia","armenia"]

print(sityvebi(sityvani))


'''Write a function that takes a list of numbers as input and returns a new list containing the square of each number.'''
def ricxvebi(ricxvebi2):
    ricxvebis_kvadratebi = []
    for d in ricxvebi2:
        ricxvebis_kvadratebi.append(d**2)
    return ricxvebis_kvadratebi

ricxvebi2 = [2,3,4,5]

print(ricxvebi(ricxvebi2))


'''Write a function that takes a list of strings as input and returns a new list containing the lengths of each string.'''
def string(stri):
    lengths_of_strings = []
    for e in stri:
        lengths_of_strings.append(len(e))
    return lengths_of_strings

stri = ["zebra","wolf","cat","dog"]

print(string(stri))


'''Write a function that takes a list of numbers as input and returns the sum of all the numbers that are greater than 10.'''
def num_func(nums_func):
    sum_of_nums_graearer_than_10 = 0
    for f in nums_func:
        if f > 10:
            sum_of_nums_graearer_than_10 += f
    return sum_of_nums_graearer_than_10

nums_func = [2,15,14,16,4,5,6]

print(num_func(nums_func))