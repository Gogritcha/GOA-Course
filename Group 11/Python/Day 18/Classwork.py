num = int(input("Enter how many number you want to input: "))
list1 = []
list2 = []
list3 = []
sum = 0
for i in range(0,num):
    num = int(input("Enter a number: "))
    if num > 10 and num % 2 == 0:
        list2.append(num)
    list1.append(num)
    sum += num
for l in range(min(list1),max(list1)+1):
    if l in list1:
        list3.append(l)
print(sum)
print(list2)
print(list3)


# def rectangle_area(Length,Width):
#     if Length == Width:
#         print("This is a square and its area is: ")
#         Area = Length*Width
#         print(Area)
#     elif Length <= 0 or Width <= 0:
#         print("You must have incorrectly inputed Length or Width, posebly both.")
#     else:
#         print("this rectangles area is: ")
#         Area = Length*Width
#         print(Area)

# Length = int(input("What is length of the rectangle that you want to calculate area for: "))
# Width = int(input("What is Width of the rectangle that you want to calculate area for: "))

# rectangle_area(Length,Width)