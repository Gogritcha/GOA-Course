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