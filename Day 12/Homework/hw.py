num = int(input("Please eter any number: "))
if num > 0:
    print("Your number is positive")
elif num < 0:
    print("Your number is negative")
else:
    print("Your number is zero")


choise = input("Chosse which one you want to convert to other: ")
if choise == "kilometer - mile":
    kilometer = float(input("Please enter how much kilometer you want to convert into miles: "))
    print(kilometer/1.609)
if choise == "mile - kilometer":
    mile = float(input("Please enter how much mile you want to convert into kilometers: "))
    print(mile*1.609)
if choise != "kilometer - mile" and choise != "mile - kilometer":
    print("You must have gotten something wrong please try again")

Name = input("Please enter your name: ")
Surname = input("Please enter your surname: ")
Age = int(input("Please enter your age: "))
Email = input("Please enter your email: ")
if Age < 13:
    print("Acsess denied")
if Age >= 13:
    print("Name =",Name)
    print("Surname =",Surname)
    print("Age =",Age)
    print("Email =",Email)


num1 = int(input("Pleae enter first number: "))
num2 = int(input("Pleae enter second number: "))
num3 = int(input("Pleae enter third number: "))
print((num1 + num2 + num3)/3)


num = int(input("Pleae enter any number between 0-10: "))
if 10 <= num or 0 >= num:
    print("That number is not between 0-10")
if 10 > num > 0:
    for num in range(num, 50, num):
        print(num)


number1 = int(input("Pleae enter first number: "))
number2 = int(input("Pleae enter second number: "))
for i in range(number1,number2 + 1):
    print(i*i*i)


user_num = input("Enter number here: ")
sum = 0
for i in user_num:
    sum += int(i)
print(sum)



numb = int(input("Pleae enter any number: "))
numbe = numb*10
o = 1
while o != 11:
    print(numb * o)
    o = o + 1


n1 = int(input("Pleae enter first number: "))
n2 = int(input("Pleae enter first number: "))
op = input("What operation do you wan tpreformed on this numbers: ")
if op == "addition":
    print(n1 + n2)
if op == "subtraction":
    print(n1 - n2)
if op == "multiplication":
    print(n1*n2)
if op == "division":
    print(n1/n2)
else:
    print("that is not math operations")


string = input("Enter anything: ")
repet = int(input("Enter how many times do you want "+string+" to get repeted: "))
for _ in range(repet):
    print(string)


kilogram = int(input("Please enter how much you weight in kilograms: "))
meter = int(input("Please enter how tall you are in meters: "))
bmi = kilogram/(meter*meter)
print (bmi)


Year = int(input("Please enter year you want to find out if it is leap year or not: "))
if Year % 4 == 0:
    print("That year is leap year")
else:
    print("That year is not leap year")


numbeer = int(input("Enter number between 0-6: "))
if 0 >= numbeer or 6 <= numbeer:
    print("Invalid input")
else:
    print("Valid input")