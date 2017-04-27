"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""

    item_to_add = raw_input("What do you like to add?")
    my_list.append(item_to_add) 
    print my_list





def view_list(my_list):
    """Print each item in the list."""
    for item in my_list:
        print item 

    #print "The view_list function has not yet been written"


def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""


    user_options = """
    \nWould you like to:
    A. Add a new item
    B. View list
    C. Quit the program
    >>> """

    print user_options

    while True:

        option = raw_input("What do you like to do?")
        if option == "A":
            add_to_list(my_list)
        elif option == "B":
            view_list(my_list)
        elif option == "C":
            break        

        # Collect input and include your if/elif/else statements here.
       

#-------------------------------------------------

my_list = []
display_main_menu(my_list)

