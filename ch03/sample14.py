your_book = [2004, 'python', 200, 'class 1']
#             0      1        2      3

new_book = your_book

print('-'*50)
print(your_book)
print(new_book)

your_book[0] = 2025

print('-'*50)
print(your_book)
print(new_book)

new_book = your_book[:]
print('-'*50)
print(your_book)
print(new_book)

your_book[0] = 2026
print('-'*50)
print(your_book)
print(new_book)