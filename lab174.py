'''
PRINT working directory, user, datetime
GET username
DEFINE functions:
    read_unpickle: OPEN 'address_book.dat' in reading mode to variable out_file
                   READ out_file AND ASSIGN to address_book
                   RETURN address_book
    write_pickle: OPEN 'address_book.dat' in writing mode to variable in_file
                  WRITE address_book to in_file
    look_up: GET name
             IF name is in address_book keys THEN
                RETURN Name: key = name, Email: value
             ELSE RETURN not found
    add_item: GET name, email
              ADD kay value pair (name, email) to address_book
    change_item: GET name, email
                 IF name is in the address_book keys THEN
                    UPDATE key value pair (name, value) with email
                    RETURN info updated
                 ELSE RETURN not found
    del_item: GET name
              TRY
                DELETING name key from address_book
                PRINT success
              IF EXCEPT THEN PRINT not found
SET nextEntry to True
CALL read_unpickle
WHILE nextEntry is True
    PRINT menu
    GET choice
    IF choice is 1 THEN
        CALL look_up()
    ELIF choice is 2 THEN
        CALL add_item()
    ELIF choice is 3 THEN
        CALL change_item()
    ELIF choice is 4 THEN
        CALL del_item()
    ELIF choice is 5 THEN
        CALL write_pickle
        PRINT info saved
        break
    ELSE
        PRINT invalid choice

'''

import os
import time
import pickle

print(f'Working Directory: {os.getenv("PWD")}')
print(f"Programmer: {os.getenv('USER')}")
print(f"Lab 17.4: {time.strftime('%B %d, %Y @ %I:%M%p')}\n")

username = input("Enter your name: ")
line = "-"*40
LOOK = 1
ADD = 2
CHANGE = 3
DEL = 4
QUIT = 5
eof = False


def read_unpickle(eof):
    out_file = open('address_book.dat', 'rb')
    while not eof:
        try:
            read_address_book = pickle.load(out_file)
        except EOFError:
            eof = True
    out_file.close()
    return read_address_book


def write_unpickle(new_entry):
    in_file = open('address_book.dat', 'wb')
    pickle.dump(new_entry, in_file)
    in_file.close()


def look_up():
    name = input("Enter name: ")
    name = name.title()
    if name in address_book.keys():
        return f"Name: {name}\nEmail: {address_book[name]}"
    else:
        return 'The specified name was not found'


def add_item():
    name = input("Enter name: ")
    name = name.title()
    email = input("Enter email address: ")
    try:
        address_book[name] = email
        return "Name and address have been added."
    except:
        return f"Name {name} already exists"


def change_item():
    name = input("Enter name: ")
    name = name.title()
    if name in address_book.keys():
        email = input("Enter new email address: ")
        address_book[name] = email
        write_unpickle(address_book)
        return "Information has been updated."
    else:
        return 'The specified name was not found'


def del_item():
    name = input("Enter name: ")
    name = name.title()
    try:
        del address_book[name]
        print('Information has been removed.')
        write_unpickle(address_book)
    except:
        print('The specified name was not found')

def display_menu():
    return f"\n{'Menu':^40}\n{line}\n" \
           f"1. Look up an email address\n"\
          f"2. Add a new name and email address\n"\
          f"3. Change an existing email address\n"\
          f"4. Delete a name and email address\n"\
          f"5. Quit the program\n"

nextEntry = True
address_book = read_unpickle(eof)
while nextEntry:
    print(display_menu())
    print(f"{username.title()}, enter your choice: ", end="")
    choice = eval(input())
    if choice == LOOK:
        print(look_up())
    elif choice == ADD:
        print(add_item())
    elif choice == CHANGE:
        print(change_item())
    elif choice == DEL:
        del_item()
    elif choice == QUIT:
        write_unpickle(address_book)
        print("Information has been saved")
        break
    else:
        print("Invalid choice. Please enter numbers from the menu (1-5)")
