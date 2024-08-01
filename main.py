#Packages

import random

# Defining values
num_rooms = 100 # How many rooms there will be.

valid_rooms = [] # The rooms that are not taken
invald_rooms = [] # The rooms that are taken


customers = [] # The details about the customers

cust_names = [] # Where the full name of the customers are going to be stored

old_cust = [] # To prevent any overlapping of names

# Generate one time use room generation
def room_gen():
    room_number = 1
    for x in range(num_rooms):
        valid_rooms.append(room_number)
        room_number += 1
room_gen()

# System structure

# How the customers will be checked in
def check_in():
    global cust_names
    name_check = True
    while name_check == True:
        print("-_-_-_-_-_-_-_-_-Check in-_-_-_-_-_-_-_-_-\n\n")
        print("Say '!cancel' to cancel the operation\n\n")
        full_name = input("Please enter the first and second name of the customer: ").lower()
        if full_name == "!cancel":
            name_check = False
            menu()
        else:
            check_val_name = full_name.split()
            if len(check_val_name) == 2:
                name_check = False
                full_name1 = full_name
                full_name_ori = full_name
                if full_name.lower() in cust_names:
                    full_name1 = full_name+f"({cust_names.count(full_name)+old_cust.count(full_name)})"
                print("Name approved.")
                cust_names.append(full_name_ori.lower())
                firstname = check_val_name[0]
                secondname = check_val_name[1]
            else:
                print("The name is invalid.")

        room_loop = True
        global valid_rooms
        global invald_rooms
        custroomnumber = False
        while room_loop == True: # Checks if the room is valid
            print(f"\n\nValid rooms:\n\n{valid_rooms}")
            choice = input(f"\nWhat room number: ")
            if choice == "":
                pass
            else:
                if choice in str(valid_rooms):
                    custroomnumber = int(choice)
                else:
                    pass

            room_ava_check = valid_rooms.count(custroomnumber)
            if room_ava_check > 0:
                customers.append(f"Full_name: {full_name1} First_name: {firstname} Second_name: {secondname} Room_number: {custroomnumber}")
                valid_rooms.remove(custroomnumber)
                invald_rooms.append(custroomnumber)
                print("Room number approved.")
                room_loop = False
                menu()
            else:
                print("Room number is invalid.")
def autofill():
    firstnames = ["Bob","James","Jess","Jessica","Jessi","Tom","Tommy","Bobby","Larry","Gary","Alex","Axel",
             "Sam","Jamie","Tyrone","Tiger","Arther","Cat","Izzy","Lilly","Jack","Jackie","Ellie","Jake","Andy",
             "Sue","Gerald","Tim","Timmy","Merhey","Harvey","Ella","Sophie","Sapphire","Leo","ALfie","Richard","Rob","Gorden"]
    
    secondnames = ["Anderson","Addson","Robinson","Bobson","Birling","Cratchit","Indictson","Fran","Poppinson",
                  "Genrichson","Barn","Pocketrocket","Yumstire","Lipson","Smith","Crabson","Raveson","Plopson","Bethson",
                  "Mcdonald","Bucket","Dickson","Ricktson","Ramsey"]

    for x in range(num_rooms):
        names = []
        while True:
          first_name = random.choice(firstnames).lower()
          second_name = random.choice(secondnames).lower()
          full_name = first_name+" "+second_name
          if any(full_name) not in names:
            names.append(full_name)
            break
        room_number = random.choice(valid_rooms)
        full_name1 = full_name
        if full_name.lower() in cust_names:
           full_name1 = full_name+f"({cust_names.count(full_name)+old_cust.count(full_name)})"
        customers.append(f"Full_name: {full_name1} First_name: {first_name} Second_name: {second_name} Room_number: {room_number}")
        cust_names.append(full_name.lower())
        valid_rooms.remove(room_number)
        invald_rooms.append(room_number)
    sort_rooms()
    print("Completed!\n\n")
    menu()


def sort_rooms():
            if len(valid_rooms) > 1:
                sort = True
                numcheck1 = 0
                numcheck2 = 1
                correct_order = 0
                while sort == True:

                    if numcheck2 == num_rooms-len(invald_rooms):
                        numcheck1 = 0
                        numcheck2 = 1

                    if correct_order == num_rooms:
                        sort = False
                
                    if valid_rooms[numcheck1] > valid_rooms[numcheck2]:
                        subject1 = valid_rooms[numcheck1]
                        subject2 = valid_rooms[numcheck2]
                        valid_rooms[numcheck1] = subject2
                        valid_rooms[numcheck2] = subject1
                        correct_order = 0
                    else:
                        correct_order += 1
                    numcheck1 += 1
                    numcheck2 += 1

# Checks the users out
def check_out():
    checking_out = True
    while checking_out == True:
        print("-_-_-_-_-_-_-_-_-Check out-_-_-_-_-_-_-_-_-\n\n")
        print("Say '!cancel' to cancel the operation\n\n")
        choice = input("\n\nEnter the full name of the customer to check out: ").lower()
        if choice == '!cancel':
            checking_out = False
            menu()
        else:
            positions = len(customers)-1
            sorted_positions = 0
            searching = True # Checking if there is an existing name in the customers list
            matched = False
            while searching == True:
                segment = customers[sorted_positions].split()
                fullname = segment[1]
                fullname = fullname+" "+segment[2]
                if choice == fullname.lower():
                    searching = False
                    checking_out = False
                    matched = True
                    print("Found match")
                    room_number = segment[8]
                    invald_rooms.remove(int(room_number))
                    true_name = segment[4]
                    true_name = true_name+" "+segment[6]
                    if cust_names.count(true_name) > 1:
                        old_cust.append(true_name)
                    cust_names.remove(true_name)
                    valid_rooms.append(int(room_number))
                    if old_cust.count(customers[sorted_positions]) > 0:
                        if customers[sorted_positions] == 0:
                            sq = old_cust.count(customers[sorted_positions])
                            for x in range(sq):
                                old_cust.remove(old_cust.count(customers[sorted_positions]))
                    customers.remove(customers[sorted_positions])
                    sort_rooms()
                    print("Customer successfully checked out.\n\n")
                    menu()
                else:
                    sorted_positions += 1
                    if sorted_positions == len(customers):
                        searching = False
                        matched = False
                        print("No match cannot be found.\n\n")

def view_rooms():
    print("-_-_-_-_-_-_-_-_-Room View-_-_-_-_-_-_-_-_-\n\n")
    print("Rooms that aren't taken:\n")
    print(f"{valid_rooms}\n")
    print("Rooms that are taken:\n")
    print(f"{invald_rooms}\n")
    print("The customers:\n")
    print(f"{customers}\n")
    choice = input("Press enter to continue: ")
    print("\n\n")
    if choice == "!cust_names":
        print(f"Names of the dwellers:\n{cust_names}")
        input("\n\nPress enter to continue: ")
        print("\n\n")
    menu()

def menu():
    menu_loop = True
    while menu_loop == True:
        print("-_-_-_-_-_-_-_-_-Menu-_-_-_-_-_-_-_-_-\n\n")
        print("1. Check in a customer")
        print("2. Check out a customer")
        print("3. View the invalid and valid rooms")
        choice = input("\n\n: ")

        if choice == "1":
            if len(valid_rooms) == 0:
                input("\n\nThere is no one to check in. Press enter to continue: ")
                print("\n\n")
            else:
                menu_loop = False
                check_in()
   
        if choice == "2":
               if len(invald_rooms) == 0: 
                input("\n\nThere is no one to check out. Press enter to continue: ")
                print("\n\n")
               else:
                   menu_loop = False
                   check_out()

        if choice == "3":
            menu_loop = False
            print("\n\n")
            view_rooms()

        if choice == "!autofill":
          print("W.I.P")  
          autofill()
menu()
