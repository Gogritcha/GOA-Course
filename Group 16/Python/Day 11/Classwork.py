age = int(input("Please enter your age: "))
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")



money = int(input("please enter how much money you have: "))
if money < 100:
    print("Not enough money")
else:
    print("You have enough money")


i = 2
while i <= 20 :
    print(i)
    i = i + 2


i = 100
while i >= 0:
    print(i)
    i = i - 1


sum = 0
i = 50
while i <= 100:
    print(sum)
    i = i + 5
    sum = sum + i



sum = 0
i = 1
while i <= 100:
    print(sum)
    i = i + 1
    sum = sum + i



number = int(input("Enter any number: "))
while number % 2 == 0:
    number = number / 2
    print(number)