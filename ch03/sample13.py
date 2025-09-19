
my_book = (2004, 'python', 200, 'class 1')
your_book = [2004, 'python', 200, 'class 1']
#             0      1        2      3

other_book = your_book

print(my_book)
print(your_book)
print(other_book)

print(id(my_book))
print(id(your_book))
print(id(other_book)) # your_book & other_book's id is same

# so if other_book is changed, your_book also changed in automate
# (but if copied like 'other_book = your_book[0:4]', don't change at all
other_book[0] = 2025
print(my_book)
print(your_book)
print(other_book)

new_book = your_book[1:2 + 1]
print(new_book)

new_book2 = my_book[1:3]
print(new_book2)