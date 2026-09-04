books = ["Python", "Java", "C++", "HTML"]

new_book = input("Enter new book: ")
books.append(new_book)

search = input("Enter book to search: ")

if search in books:
    print("Book found")
else:
    print("Book not found")

remove = input("Enter book to remove: ")

 if remove in books:
    books.remove(remove)

print("Books:", books)

print("Total books:", len(books))