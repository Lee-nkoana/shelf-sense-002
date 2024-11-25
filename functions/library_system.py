DATABASE_FILE = "./database/books.txt"

def initialize_database():
    """
    Initialize the database file if it doesn't exist.
    """
    with open(DATABASE_FILE, 'a') as db:
        
        pass  # Ensure the file exists

def add_book(title, author):
    """
    Add a new book to the library.
    :param title: The title of the book
    :param author: The author of the book
    """
    # TODO: Append the book's title and author to the database file
    with open(DATABASE_FILE, 'a') as db:   
        book_info = f"{title}, {author}"
        db.writelines(book_info)


def search_book(title):
    """
    Search for a book by title.
    :param title: The title of the book to search for
    :return: A dictionary with the book's details if found, else None
    """
    
    # TODO: Implement logic to search for a book in the database file
    book_dict = {}
    with open(DATABASE_FILE, 'r') as db:   
        books = db.readlines()
        book_title = books.split(",")[0]
        book_author = books.split(",")[1]
    
    for i, author in books:
        if title == book_title:
            book_dict[title] = author
    return book_dict

def list_books(database):
    """
    List all books in the library.
    :return: A list of dictionaries with each book's details
    """
    # TODO: Read all books from the database file and return them as a list of dictionaries
    books_dict = {}
    with open(database, 'r') as db:   
        books = db.readlines()
        print(books)

    for book in books:
        title = book.split(",")[0]
        author = book.split(",")[1]
    
        books_dict[title] =  author
    return books_dict
    

list_books(DATABASE_FILE)