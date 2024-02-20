#declaring value of first prices for 10 books
book1_first_price = 9
book2_first_price = 13
book3_first_price = 11
book4_first_price = 26
book5_first_price = 25
book6_first_price = 16
book7_first_price = 17
book8_first_price = 18
book9_first_price = 15
book10_first_price = 10

#declaring a variable of discount for books 1-5
discount = 10

#declaring a variable of discount for books 5-10
discount2 = 20

#declaring value of price after discount for books 1-10
book1_price_after_discount = book1_first_price - book1_first_price * discount / 100
book2_price_after_discount = book2_first_price - book2_first_price * discount / 100
book3_price_after_discount = book3_first_price - book3_first_price * discount / 100
book4_price_after_discount = book4_first_price - book4_first_price * discount / 100
book5_price_after_discount = book5_first_price - book5_first_price * discount / 100
book6_price_after_discount = book6_first_price - book6_first_price * discount2 / 100
book7_price_after_discount = book7_first_price - book7_first_price * discount2 / 100
book8_price_after_discount = book8_first_price - book8_first_price * discount2 / 100
book9_price_after_discount = book9_first_price - book9_first_price * discount2 / 100
book10_price_after_discount = book10_first_price - book10_first_price * discount2 / 100

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