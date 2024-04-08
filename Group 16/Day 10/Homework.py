for i in range (20 + 1):
    print(i)


i = 50
sum = 0
for i in range (50, 100 + 1):
    sum += i
    print(sum)


for i in range(-10, 10, 3):
    print(i)


num1 = int(input("Please etner first number: "))
num2 = int(input("Please etner second number: "))
i = num1 > num2
a = 0
if i == True:
    for a in range(num2, num1, 2):
        print(a)
else:
    print("no")


num1 = int(input("Please etner first number: "))
num2 = int(input("Please etner second number: "))
i = num1 > num2
a = 0
sum = 0
if i == True:
    for a in range(num2, num1):
        sum += a
        print(sum)
else:
    print("no")