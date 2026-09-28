#mini LIBRARY MANAGEMENT SYSTEM

library = ["Harry potter","Java programming","Python Programming","Goosebumps",
           "The Habbit",
          "The Alchemist",
         "1984",
         "Animal Farm",
          "The Great Gatsby",
         "Pride and Prejudice",
         "Atomic Habits",
         "Wings of Fire",
         "Python Crash Course",
         "Python cookbook",
         "Harry Potter and the Chamber of Secrets",
         "Harry Potter and the Prisoner of Azkaban",
         "Harry Potter and the Goblet of Fire",
         "Engineering Mathematics","Alice in the Wonderland",
         "Thermodynamics","Fluid Mechanism",
         "Programming in C","Rich Dad Poor Dad", "Adventures of Tom Sawyer", "Concise chemistry","Concise mathematics"]




def add_books():  #FOR ADDING BOOKS IN LIBRARY
    book= input("enter book name to be added")
    library.append(book)
    print(f"{book} is added successfully!")  

        

def issue_books(): #FOR ISSUING BOOKS
    book = input("Enter book name to be issued: ").lower()

    for available_book in library:
        if available_book.lower() == book:
            print(f"{available_book} has been issued successfully!")
            library.remove(available_book)  
            return

    print("sorry,book unavaiable")     




def view_books(): #FOR VIEWING LIST OF BOOKS AVAILABLE
    if not library:
        print("no books present right now")
    else:
        print("list of books")
        idx=1
        for books in library:
            print(f"{idx}.  {books}")
            idx=idx+1
            print()



def search_books(): #FOR SEARCHING PARTICULAR BOOK
    book= input("enter book name to search")
    if book in library:
        print("book is available")
    else:
        print("sorry, book currently unavailable")




def return_books(): #FOR RETURNING BOOKS AND CHECKING FINE
    book= input("enter name of book to return")
    if book not in library:
        days= int(input("enter number of days book was kept: "))
        #FINE IS RUPEES 20 PER DAY AFTER 10 DAYS
        if days>10:
            fine= (days-10)*20
            print("late return!")
            print("please proceed the fine payment of rupees",fine)
        else:
            print("thankyou!please visit us again")
        library.append(book)

    else:
        print("this book was not issued")



while(True):
    print("------------WELCOME TO LIBRARY MANAGEMENT SYSTEM--------------")
    print("1.Add books")
    print("2.Issue books")
    print("3.Search books")
    print("4.View books")
    print("5.Return book")
    print("6.Exit")


    choice= input("enter your choice")
    if choice=="1":
        add_books()
    elif choice=="2":
        issue_books()
    elif choice=="3":
        search_books()
    elif choice=="4":
        view_books()
    elif choice=="5":
        return_books()
    elif choice=="6":
        print("Thankyou for choosing our library visit us soon!")
        break
    else:
        print("invalid choice!please try again")
