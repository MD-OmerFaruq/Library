class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)

class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability
        Library.entry_book(self)

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print()
            print(f"Book '{self.__title}' borrowed successfully.")
            print()
        else:
            print()
            print(f"Book '{self.__title}' is already borrowed.")
            print()

    def return_book(self):
        if self.__availability == 0:
            self.__availability = True
            print()
            print(f"Book '{self.__title}' returned successfully.")
            print()
        else:
            print()
            print(f"Book '{self.__title}' was not borrowed.")
            print()

    def view_book_info(self):
        if self.__availability == 1:
            availability_status = "Available" 
        else:
            availability_status = "Not Available"
        print(f"ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: {availability_status}")

    # private access er jonno
    @property       
    def book_id(self):
        return self.__book_id

    @property
    def availability(self):
        return self.__availability


def display_menu():
    print("-----Welcome to the Library-----")
    print("1. View All Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")
    print('--------------------------------')


def main():
    Book(101, "Python Programming", "John Doe")
    Book(102, "Data Science Essentials", "Jane Smith")
    Book(103, "Machine Learning", "Alan Turing")
    Book(104, "Artificial Intelligence", "Marvin Minsky")
    Book(105, "Deep Learning", "Yann LeCun")
    Book(106, "Natural Language Processing", "Christopher Manning")
    Book(107, "Statistics for Data Science", "David C. Hsu")
    Book(108, "Python for Data Analysis", "Wes McKinney")

    while 1:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print()
            print("Library Books:")
            for book in Library.book_list:
                book.view_book_info()
            print()

        elif choice == "2" :
            try:
                book_id = int(input("Enter book ID to borrow: "))
                book = 0
                for b in Library.book_list:
                    if b.book_id == book_id:
                        book = b
                        break
                if book:
                    book.borrow_book()
                else:
                    print("Invalid book ID.")
            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "3" :
            try:
                book_id = int(input("Enter book ID to return: "))
                book = 0
                for b in Library.book_list:
                    if b.book_id == book_id:
                        book = b
                        break
                if book:
                    book.return_book()
                else:
                    print("Invalid book ID.")
            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "4":
            print("Exiting the Library System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again...")


main()

