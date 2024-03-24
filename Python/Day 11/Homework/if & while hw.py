num = int(input("Please try to guess my number: "))
while num != 5:
    num = int(input("Your number was wrong please try again: "))
if num == 5:
    print("You are right!")


num1 = int(input("Please enter even number: "))
while num1 % 2 != 0:
    print("Your number is odd")
    num1 = int(input("Please enter even number: "))
if num1 % 2 == 0:
    print("your number is even")


sum=0
for i in range(50, 101):
    if i%2==1:
        print(i)
    if i>75:
        sum = sum + i
print(sum)


user_num = int(input("Enter your number: "))
updated_num = user_num + 20
while user_num < updated_num:
    print(user_num)
    user_num += 1


name = (input("Please enter this code's creators name: "))
while name != "Nikoloz Gogritchiani":
    print("that is not right try again: ")
    name = (input("Please enter this code's creators name: "))
if name == "Nikoloz Gogritchiani":
    print("Thats right")