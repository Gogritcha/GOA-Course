#declaring value of starting
#prices for 10 books
book1_starting_price = 9
book2_starting_price = 13
book3_starting_price = 11
book4_starting_price = 26
book5_starting_price = 25
book6_starting_price = 16
book7_starting_price = 17
book8_starting_price = 18
book9_starting_price = 15
book10_starting_price = 10

#declaring a variable of discount for books 1-5
discount1 = 10

#declaring a variable of discount for books 5-10
discount2 = 20

#declaring value of price after discount for books 1-10
book1_price_after_discount = book1_starting_price - book1_starting_price * discount1 / 100
book2_price_after_discount = book2_starting_price - book2_starting_price * discount1 / 100
book3_price_after_discount = book3_starting_price - book3_starting_price * discount1 / 100
book4_price_after_discount = book4_starting_price - book4_starting_price * discount1 / 100
book5_price_after_discount = book5_starting_price - book5_starting_price * discount1 / 100
book6_price_after_discount = book6_starting_price - book6_starting_price * discount2 / 100
book7_price_after_discount = book7_starting_price - book7_starting_price * discount2 / 100
book8_price_after_discount = book8_starting_price - book8_starting_price * discount2 / 100
book9_price_after_discount = book9_starting_price - book9_starting_price * discount2 / 100
book10_price_after_discount = book10_starting_price - book10_starting_price * discount2 / 100

#showing final prices

print(book1_price_after_discount)
print(book2_price_after_discount)
print(book3_price_after_discount)
print(book4_price_after_discount)
print(book5_price_after_discount)
print(book6_price_after_discount)
print(book7_price_after_discount)
print(book8_price_after_discount)
print(book9_price_after_discount)
print(book10_price_after_discount)