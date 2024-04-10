def even_counter(numbers):
    count = 0
    for a in numbers:
        if a % 2 == 0:
            count += 1
    return count

print(even_counter([1,2,3,4,5,6,7,8,9,10]))


def even_index_replacer(str_or_list,replacer_char):
    replaced = ""
    for i in range(len(str_or_list)):
        if i % 2 == 0:
            replaced += replacer_char
        else:
            replaced += str_or_list[i]
    return replaced

print(even_index_replacer("Buildings", "l"))


def last_even_index(list):
    for index in range(len(list)-1,-1,-1):
        if list[index] % 2 == 0:
            return index
        
print(last_even_index([1,2,3,4,5,6,7,8,9,10,2]))