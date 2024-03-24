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