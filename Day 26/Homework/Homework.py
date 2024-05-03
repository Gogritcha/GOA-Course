def manual_sum(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

numbers = [1,2,4,5,67,32,54]
print(manual_sum(numbers))


def manual_max(nums):
    s = 0
    for a in nums:
         if a > s:
            s = a
    return s

nums = [1,2,3,4,6,7,8,60,4,17,34]
print(manual_max(nums))


def manual_min(num_list):
    g = ""
    a = True
    for i in num_list:
        if a == True:
            g += str(i)
            a = False
        if i < int(g):
            g = i
    return g

num_list = [2,3,4,5,6,-999,7,8,9,1]
print(manual_min(num_list))


def manual_len(listy):
    f = 0
    for h in listy:
        f += 1
    return f

listy = [1,2,3,4,5,6,7,8]
print(manual_len(listy))


def manual_reduce(copy_needing_list):
    copyed_list = []
    for q in copy_needing_list:
        copyed_list.append(q)
    return copy_needing_list, copyed_list

copy_needing_list = [1,"faa",2,"hello",4,5,7,"9"]
print(manual_reduce(copy_needing_list))