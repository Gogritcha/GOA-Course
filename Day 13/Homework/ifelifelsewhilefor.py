age = int(input("Please enter your age: "))
if 65 > age > 18:
    print("You are an adult")
elif  age < 18:
    print("You are a minor")
else:
    print("You are a senior citizen.")


num1 = int(input("Pleae enter first number: "))
num2 = int(input("Pleae enter second number: "))
num3 = int(input("Pleae enter third number: "))
num4 = int(input("Pleae enter fourth number: "))
num5 = int(input("Pleae enter fifth number: "))
if num1 % 2 == 0:
    print("First number is even")
else:
    print("First number is odd")
if num2 % 2 == 0:
    print("Second number is even")
else:
    print("Second number is odd")
if num3 % 2 == 0:
    print("Third number is even")
else:
    print("Third number is odd")
if num4 % 2 == 0:
    print("Fourth number is even")
else:
    print("Fourth number is odd")
if num5 % 2 == 0:
    print("Fifth number is even")
else:
    print("Fifth number is odd")


grade = input("what grade did you get A, B, C, D or F: ")
if grade == "A":
    print("Excellent!")
elif grade == "B":
    print("Good job!")
elif grade == "c":
    print("You passed.")
elif grade == "D":
    print("You can do better.")
elif grade == "F":
    print("You failed.")
else:
    print("You must have gotten something wrong try again")


i = 1

while i <= 10:
    print(i)
    i = i + 1


num = 7
guess_num = int(input("Try to guess my number, it is 1 through 10: "))
while guess_num != num:
    guess_num = int(input("Wrong try again: "))
print("You are correct!")


b = int(input("Enter number: "))
a = b
c = b * 10
while b <= c:
    print(b)
    b += a


i = 10

while i >= 1:
    print(i)
    i = i - 1