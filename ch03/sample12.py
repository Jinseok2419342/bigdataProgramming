your_book = [2002, 'python', 'python', 'python', 200]
print(type(your_book))
print(your_book)

# can data change
your_book[0] = 25
print(your_book)

# also can add
your_book.append('python programming')
print(your_book)

your_book.insert(1, 'programming subject')
print(your_book)

# delete
if 'python2' in your_book:
    your_book.remove('python2')
print(your_book)
