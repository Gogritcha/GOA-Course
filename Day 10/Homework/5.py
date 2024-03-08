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