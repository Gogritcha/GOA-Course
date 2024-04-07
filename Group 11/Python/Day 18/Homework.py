'''შექმენით ფუნქცია, რომელსაც გადაეცემა 1-იდან 20-ის ჩათვლით რიცხვების სია. თქვენ უნდა დააბრუნოთ გაფილტრული სია, სადაც უკვე მარტო 4-ის ჯერადები იქნება.'''

def nums():
    list = []
    for i in range(1,21):
        if i % 4 == 0:
            list.append(i)
    print(list)

nums()


'''შექმენით ფუნქცია, რომელსაც გადასცემთ მომხმარებლისგან მიღებულ სახელსა და გვარს. შემდეგ ისინი დაამატეთ სიაში და დააბრუნეთ სია'''

list1 = []

def info():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    return name,surname
list1.append(info())
print(list1)


'''მომხმარებელს შეეკითხეთ საწყისი და საბოლოო რიცხვები. ეს რიცხვები გადაეცით ფუნქციას, for ციკლით სიაში შეინახეთ მათ შორის არსებული რიცხვები. შემდეგ მოახდინეთ გაფილტვრა, ისევ for 
ციკლით განიხილეთ თითოეული რიცხვი - თუ რიცხვი ლუწი იქნება, ახალ სიაში დაამატეთ მისი მეორე ხარისხი, ხოლო თუ კენტი იქნება სიაში დაამატეთ მისი კვადრატული ფესვი (0.5 ხარისხი).'''

every_num = []
even_nums_squared = []
odd_nums_square_root = []
start = int(input("a"))
end = int(input("a"))
def nums():
    for i in range(start,end+1):
        every_num.append(i)
        if i % 2 == 0:
            even_nums_squared.append(i**2)
        else:
            odd_nums_square_root.append(i**0.5)
    print(every_num)
    print(even_nums_squared)
    print(odd_nums_square_root)

nums()


'''შექმენით ფუნქცია, რომელსაც გადასცემთ მომხმარებლის გვარს. გვარის თითოეული ასო გადაიტანეთ ახალ სიაში. შემდეგ for ციკლის გამოყენებით იმუშავეთ ამ სიაზე - მარტო ლუწ ინდექსებზე 
მყოფი ასოები დაამატეთ ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია.
Bonus (არაა სავალდებულო): ეს სია გარდაქმენით სთრინგად და ამ სახით დააბრუნეთ.'''

def sur_index():
    sur = input("Enter your surname: ")
    x = 1
    sur_ = []
    while len(sur) != len(sur_):
        sur_.append(sur[x])
        x += 2
        if x >= len(sur):
            break
    print(sur_)
sur_index()



'''შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. თქვენ უნდა დააბრუნოთ ამ სიის საშუალო არითმეტიკული ( ჯამი / სიგრძე )'''

def avrage_calculator():
    list_of_nums = []
    avrage = 0
    sum = 0
    num = int(input("Enter how many number you want to input: "))
    for j in range(0,num):
        num = int(input("Enter a number: "))
        list_of_nums.append(num)
        sum += num
    for g in range(list_of_nums[0],list_of_nums[-1]+1):
        avrage += g
    avrage = avrage / len(list_of_nums)
    print(avrage)
avrage_calculator()


'''შექმენით ფუნქცია, რომელიც მიიღებს მომხმარებლისგან სიტყვას. შემდეგ თქვენ უნდა მოახდინოთ ამ სიტყვის შებრუნება, მაგ: word - drow. საბოლოდ კი დააბრუნეთ შედეგი.'''
word = input("Enter word and code will print its reversed veresion: ")
print(word[::-1])


'''შექმენით ფუნქცია, რომელიც მიიღებს რიცხვების სიას და თქვენ დააბრუნებთ მის გაფილტრულ ვერსიას, რომელსაც არ ექნება დუპლიკატები (ერთი და იგივე ელემენტები).'''

def fun():
    _numbers_list_ = []
    _filtered_numbers_list_ = []
    num_ = int(input("Enter how many number you want to input: "))
    for y in range(0,num_):
        num_ = int(input("Enter a number: "))
        _numbers_list_.append(num_)
    for t in range(min(_numbers_list_),max(_numbers_list_)+1):
        if t in _numbers_list_:
            _filtered_numbers_list_.append(t)
    print(_filtered_numbers_list_)

fun()