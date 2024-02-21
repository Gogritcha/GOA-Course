#declaring prices of items below
Book = "10"
Pen = "1"
Notebook = "2"

#let's say you want to buy pen, notebook and book all together
print("That will cost you",int(Book) + int(Pen) + int(Notebook),"Lari")

#Buyin 2 pens and book
print("That will cost you",int(Pen)*2 + int(Book),"Lari")

#If you buy want to calculate whow many lari you will have after buyin all three items
Money = "20"
print("You will have", int(Money) - (int(Book) + int(Pen) + int(Notebook)),"lari")

#If you have 10% discout coupon on your whole purchase
Coupon = "10"
print("That will cost you",int(Book) + int(Pen) + int(Notebook) * (int(Coupon) / 100),"Lari instead of",int(Book) + int(Pen) + int(Notebook))