book_name = input()
book_count = 0
is_book_found = False
current_book = input()
while current_book != "No More Books":
    if current_book == book_name:
        is_book_found = True
        print(f"You checked {book_count} books and found it.")
        break
    book_count += 1
    current_book = input()

if not is_book_found:
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")

# second time solving:
# book_name = input()
# current_book = input()
# books_counter = 0
# book_not_found = False
#
# while current_book != book_name:
#     if current_book == "No More Books":
#         book_not_found = True
#         break
#     books_counter = books_counter + 1
#     current_book = input()
#
# if book_not_found:
#     print("the books is not here")
#     print(f"you checked {books_counter} books")
# else:
#     print(f"you checked {books_counter} books and found it")






















