List_of_books = [{"Title":"Ekanta","Author":"Raja ram Tandukaar","Year":2023,"status":"available"},
                 {"Title":"Pratyagaman","Author":"Laxmi Prasad Devkota","Year":2021,"status":"available"},
                 {"Title":"Muna Madan","Author":"Laxmi Prasad Devkota","Year":2019,"status":"unavailable"}]

def show_books():
    count=0
    print("Your books are: ")
    for i in List_of_books:
        print(f"Title: {i["Title"]}, Author: {i["Author"]}, Year of published: {i["Year"]}")
        count+=1
    
def add_book():
    Title = input("Enter name of the book you want to add: ")
    author = input("Enter name of author of the book: ")
    year = int(input("Enter published year of the book: "))
    availability = "available"
    new_book = {"Title":Title,"Author":author,"Year":year,"status":availability}
    List_of_books.append(new_book)
    print("Your book was successfully added.")

def borrow_books():
    title = input("Enter name of the book you want to borrow: ").strip()
    found = False
    for i in List_of_books:
        if i["Title"].lower() == title.lower():
            found = True
            if i["status"].lower() == "available":
                i["status"] = "unavailable"  # Mark as borrowed
                print(f"You have successfully borrowed '{i['Title']}'.")

            else:
                print(f"Sorry, '{i['Title']}' is currently unavailable.")
            break

    if not found:
        print("Book not found in the library.")

def Return_books():
    title = input("Enter name of the book you want to borrow: ").strip()
    found = False
    for i in List_of_books:
        if i["Title"].lower() == title.lower():
            found = True
            if i["status"].lower() == "unavailable":
                i["status"] = "available"  # Mark as returned
                print(f"You have successfully returned '{i['Title']}'.")

            else:
                print(f"Sorry, '{i['Title']}' is currently unavailable.")
            break

    if not found:
        print("Book not found in the library.")

def search_books():
    keyword = input("Enter keyword to search by title of the book: ")
    found = False
    print("\n Search results: ")
    for i in List_of_books:
        if keyword in i["Title"].lower():
            print(f"Name: {i["Title"]}, Author: {i["Author"]}, Year: {i["Year"]} ")
            found = True

    if not found:
        print("No msatching book found")

while True:
    print("""
        Press:
          1 to add books
          2 to view book list
          3 to borrow book
          4 to return book
          5 to search books by keyword
          6 to quit...""")
    try:
        user_input = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number: ")
        continue

    if user_input ==1:
        add_book()
    elif user_input == 2:
        show_books()
    elif user_input ==3:
        borrow_books()
    elif user_input==4:
        Return_books()
    elif user_input==5:
        search_books()
    elif user_input==6:
        break
    else:
        print("Invalid Choice. PLease try again later.")




