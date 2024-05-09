 #ვქმნით ფუნქციას რომელსაც ვარქმევთ find_last_even რადგან ეს პოულობს ლისთში ბოლო ლუწი რიცხვის ინდექსს.
def find_last_even(numbers_list):
    #for ციკლით გადავუვლიტ მლიან ლისტს, ბოლოდან დავიწყებ და ლისტსის თავში ჩამოვალთ.
    for i in range(len(numbers_list) - 1, -1, -1):
        #if ფუნქციით შევამოწმებთ ყველა რიცხვს ლისტში და ყველა ლუწი რიცხვის შემდეგ i-ს მნიშვნელობა შეიცვლება, ბოლოს i-ს ექნება ლისტის ყველაზე ბოლო ლუწი რიცხვის ინდექსის მნიშვნელობა
        if numbers_list[i] % 2 == 0:
            #return-ით ვაბრუნებთ i-ს რადგან ეს ინახავს ბოლო ლუწი რიცხვის ინდექსს.
            return i

print(find_last_even([1,2,3,4,5]))