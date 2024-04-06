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


num = int(input("Pleae enter any number: "))
if num % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")


Temp = int(input("Please enter your house temperature: "))
if Temp > 30:
    print("It is hot in your house")
if Temp < 20:
    print("It is cold in your house")
if 30 >= Temp >= 20:
    print("It is warm in your house")


Grade = int(input("Please enter your grade: "))
if 100 >= Grade >= 90:
    print("A")
if 90 > Grade >= 80:
    print("B")
if 80 > Grade >= 70:
    print("C")
if 70 > Grade >= 60:
    print("D")
if 60 > Grade >= 0:
    print("F")
else:
    print("You must have entered wrong grade please try again")


num0 = int(input("Pleae enter any number: "))
if num0 % 2 == 0:
    print("Your number can be devided by 2")
if num0 % 3 == 0:
    print("your number can be divided by 3")
if num0 % 2 != 0:
    print("Your number can not be devided by 2")
if num0 % 3 != 0:
    print("YOur number can not be devided by 3")


num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))
if num1 > num2:
    print(num1,"is bigger than",num2,"by",num1 - num2)
if num1 < num2:
    print(num2,"is bigger than",num1,"by",num2 - num1)


i = 10
while i >= 1:
    print(i)
    i -= 1
print("დრო ამოიწურა")


sum = 0
a = int(input("Please enter number: "))
while a != 0:
    sum += a
    a = int(input("Please enter number: "))
print(sum)


password = input("Please enter yout password: ")
password_check = ("nikaluka")
while password != password_check:
    password = input("Provided password was wrong please try again: ")
print("Access granted!")


c = 2
while c <= 20:
    print(c)
    c = c + 2


yum = 0
b = int(input("Please enter number: "))
while b >= 0:
    yum += b
    b = int(input("Please enter number: "))
print(yum)