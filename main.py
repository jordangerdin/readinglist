""" Program to create and manage a list of books that the user wishes to read, and books that the user has read. """

from bookstore import Book, BookStore
from menu import Menu
import ui

store = BookStore()

def main():

    menu = create_menu()

    while True:
        choice = ui.display_menu_get_choice(menu)
        action = menu.get_action(choice)
        action()
        if choice == 'Q':
            break


def create_menu():
    menu = Menu()
    menu.add_option('A', 'Add Book', add_book)
    menu.add_option('S', 'Search For Book', search_book)
    menu.add_option('U', 'Show Unread Books', show_unread_books)
    menu.add_option('R', 'Show Read Books', show_read_books)
    menu.add_option('B', 'Show All Books', show_all_books)
    menu.add_option('C', 'Change Book Read Status', change_read)
    menu.add_option('Q', 'Quit', quit_program)

    return menu


def add_book():
    try:
        new_book = ui.get_book_info()
        new_book.save()
    except:
        print("**This book is already in the store.**\n")

def show_read_books():
    read_books = store.get_books_by_read_value(True)
    ui.show_books(read_books)


def show_unread_books():
    unread_books = store.get_books_by_read_value(False)
    ui.show_books(unread_books)


def show_all_books():
    books = store.get_all_books()
    ui.show_books(books)


def search_book():
    # while true:
    search_term = ui.ask_question('Enter search term, will match partial authors or titles.')
        # if(not search_term):
        #     print("You cannot enter in a blank string")
        # else:
        #     break
    matches = store.book_search(search_term)
    ui.show_books(matches)


def change_read():
    book_id = ui.get_book_id()
    book = store.get_book_by_id(book_id)  
    
    if book is None:
        print("\n**Error: Book not found in database.**\n")
        return
    else:
        new_read = ui.get_read_value()

        if(new_read):
            print(f"\nYou have read {book.title} by {book.author}.\n")
        else:
            print(f"\nYou have not read {book.title} by {book.author}.\n")
        book.read = new_read
        book.save()


def delete_book():

    try:
        book_id = ui.get_book_id()
        book = store.get_book_by_id(book_id)
        book.delete()
        print("\nBook was successfully deleted!\n")

    except:
        print("\nError: Book Not Found\n")

    
def quit_program():
    ui.message('Thank you for using the program, Goodbye.')


if __name__ == '__main__':
    main()
