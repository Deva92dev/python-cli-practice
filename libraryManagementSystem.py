def get_correct_title():
    while True:
        title = input("What is the title of the book?: ")
        cleaned_title = title.strip()

        if cleaned_title == "":
            print("Title can not be empty.")
            title = cleaned_title
            continue

        return cleaned_title


def get_correct_author_name():
    while True:
        author = input("Who is the author of this book?: ")
        cleaned_author = author.strip()

        if cleaned_author == "":
            print("Author name can not be empty")
            author = cleaned_author
            continue

        if cleaned_author.isdigit():
            print("Author name cannot contain digits")
            continue

        return cleaned_author


def log_execution(func):
    def inner(*args):
        print("Running get count")
        func(*args)

        print("Finished get count")

    return inner


class Book:
    def __init__(self, title, author, is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def __repr__(self):
        return f"title: {self.title}, author: {self.author}, is_borrowed: {self.is_borrowed}"

    def borrow(self):
        self.is_borrowed = True
        return f"Want to borrow {self.title} book"

    def return_book(self):
        self.is_borrowed = False
        return f"Want to return {self.title} book"


class Library:
    def __init__(self):
        self.all_books = []

    def __iter__(self):
        for item in self.all_books:
            yield item

    def add_book(self, title, author, is_borrowed=False):
        book = Book(title, author, is_borrowed)
        self.all_books.append(book)
        print(f"Record for {title} added.")

    def list_book(self):
        print("all books", self.all_books)

    def remove_book(self, title):
        for item in self.all_books:
            if item.title == title:
                self.all_books.remove(item)
                return f"remaining books are {self.all_books}"

    def search_book(self, title):
        for item in self.all_books:
            if item.title == title:
                print(f"Found: {item}")
                break
        else:
            print("Not found")

    @log_execution
    def borrow_book(self, title):
        for item in self.all_books:
            if item.title == title:
                if item.is_borrowed:
                    print("Book is already borrowed")
                else:
                    item.borrow()
                    print("borrowed", item.title)
                    break
        else:
            print("The book you want to borrow is not in the library")

    @log_execution
    def return_book(self, title):
        for item in self.all_books:
            if item.title == title:
                if item.is_borrowed:
                    item.return_book()
                    print("returned", item.title)
                    break
                else:
                    print("You have already returned the book")
        else:
            print("The book you want to return does not match any book")


def borrowed_books(books):
    books = [item for item in books if item.is_borrowed]
    print("Borrowed books and length", books, len(books))


def available_books(books):
    books = [item for item in books if not item.is_borrowed]
    print("Available books and length", books, len(books))


def generate_available_books(books):
    for book in books:
        yield book


def main():
    library = Library()
    while True:
        cleaned_title = get_correct_title()
        cleaned_author = get_correct_author_name()

        library.add_book(cleaned_title, cleaned_author)
        library.list_book()

        print("Total Number of books: ", len(library.all_books))

        search_book = input("Search your book... ")
        single_book = library.search_book(search_book)
        print(single_book)

        borrowed_books(
            library,
        )
        available_books(library)
        all_available_books = generate_available_books(library)
        for item in all_available_books:
            print(item)

        user_input = input("What do you want to do? Borrow or return... ")
        if "borrow" in user_input.lower() or "b" in user_input.lower():
            library.borrow_book(cleaned_title)
        else:
            library.return_book(cleaned_title)

        search_to_remove_one_book = input("Which book do you want to remove?: ")
        remove_one_book = library.remove_book(search_to_remove_one_book)
        print(remove_one_book)


if __name__ == "__main__":
    main()
