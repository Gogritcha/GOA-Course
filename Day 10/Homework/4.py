num1 = int(input("Please etner first number: "))
num2 = int(input("Please etner second number: "))
i = num1 > num2
a = 0
if i == True:
    for a in range(num2, num1, 2):
        print(a)
else:
    print("no")