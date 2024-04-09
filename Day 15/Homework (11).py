num = int(input("Enter even number: "))
if num % 2 == 0:
    print("Your number is even.")
else:
    print("Number is no even, closet even number to your number is", num+1, "or", num-1)


inc = 0
password = "GOA_best"
guessed_password = input("Please enter you password: ")
while guessed_password != password:
    inc += 1
    print("Provided password is wrong, you have entered wrong password",inc,"amount of times. ")
    guessed_password = input("Please try again: ")
else:
    print("Access granted!")


str = input("Enter word that starts with G: ")
if str[0] == "G":
    str = True
    print(str)
else:
    str = False
    print(str)


i = 10
while i >= 0:
    print(i)
    i -= 1


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
if op == "degree":
    op2 = int(input("which number should be degree? "))
    if op2 == n1:
        print(n2**n1)
    if op2 == n2:
        print(n1**n2)
    else:
         print("please use numbers that you have inputed, reminder they are",n1,"and",n2)
else:
    print("that is not math operations")


name = input("Please enter your name: ")
print(name[-1])


list = []
num= int(input("enter number: "))
for i in range(0,num):
    list.append(i)
print(list)


