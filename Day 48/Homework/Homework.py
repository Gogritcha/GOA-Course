# def sum_two_smallest_numbers(numbers):
#     def sum_two_smallest_numbers(num_list):
#     b = []
#     c = 0
#     for i in num_list:
#         if i != min(num_list):
#             b.append(i)
#         else:
#             c += min(num_list)
#     for i in b:
#         if i == min(b):
#             c += min(b)
#     return c


# def max_multiple(divisor, bound):
#     for i in range(bound+1):
#         if i % divisor == 0:
#             a = i
#     return a


# def get_even_numbers(arr):
#     evens = []
#     for i in arr:
#         if i % 2 == 0:
#             evens.append(i)
#     return evens


# def check_exam(correct_answers,test_answers):
#     result = 0
    
#     for i in range(len(correct_answers)):
#         if correct_answers[i] == test_answers[i]:
#             result += 4
#         elif test_answers[i]  == "":
#             result += 0
#         else:
#             result -= 1
    
#     if result < 0:
#         return 0
#     else:
#         return result

print("("+234+","+253+")")