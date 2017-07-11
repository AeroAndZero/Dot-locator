import os
# TITLE
print("\n")
print("========== DOT LOCATOR V1.0 ==========")
print("Created By Ayush Thakur")
print(" ")

# coordinates' List
cor = [['.', '.', '.', '.', '.', '5', '.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.', '4', '.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.', '3', '.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.', '2', '.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.', '1', '.', '.', '.', '.', '.'],
       ['5', '4', '3', '2', '1', '0', '1', '2', '3', '4', '5'],
       ['.', '.', '.', '.', '.', '1', '.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.', '2', '.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.', '3', '.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.', '4', '.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.', '5', '.', '.', '.', '.', '.']]


def cor_print(cor):
    for i in cor:
        print(" ".join(i))

cor_print(cor)
print("- NOTE THAT THIS IS A NORMAL COORDINATE PLANE")
print("To see all the commands type help")

# for X value
cor_dict = {
        -5: 0,
        -4: 1,
        -3: 2,
        -2: 3,
        -1: 4,
        0: 5,
        1: 6,
        2: 7,
        3: 8,
        4: 9,
        5: 10
    }

# For Y Value
cor_dict_y = {
        5: 0,
        4: 1,
        3: 2,
        2: 3,
        1: 4,
        0: 5,
        -1: 6,
        -2: 7,
        -3: 8,
        -4: 9,
        -5: 10
    }

""" Records """
#rec = {}

"""  FOR ADDING A POINT"""
def add_point():
    user_x = input("Value Of X-axis : ")
    user_y = input("Value Of Y-axis : ")
#    rec[str(user_x)] = str(user_y)

    if int(user_y) > 0:

        if int(user_x) > 0:
            cor[6 - int(user_y) - 1][cor_dict[int(user_x)]] = 'O'
            print(cor_print(cor))

        elif int(user_x) <= 0:
            cor[6 - int(user_y) - 1][cor_dict[int(user_x)]] = 'O'
            print(cor_print(cor))

    if int(user_y) <= 0:

        if int(user_x) > 0:
            cor[cor_dict_y[int(user_y)]][cor_dict[int(user_x)]] = 'O'
            print(cor_print(cor))

        elif int(user_x) <= 0:
            cor[cor_dict_y[int(user_y)]][cor_dict[int(user_x)]] = 'O'
            print(cor_print(cor))


"""
    FOR CLEARING A POINT
"""
def clear():
    print("Clearing a Point")
    user_x = input("Value Of X-axis : ")
    user_y = input("Value Of Y-axis : ")
#    del rec[str(user_x)]

    if int(user_y) > 0:

        if int(user_x) > 0:
            cor[6 - int(user_y) - 1][cor_dict[int(user_x)]] = '.'
            print(cor_print(cor))

        elif int(user_x) <= 0:
            cor[6 - int(user_y) - 1][cor_dict[int(user_x)]] = '.'
            print(cor_print(cor))

    if int(user_y) <= 0:

        if int(user_x) > 0:
            cor[cor_dict_y[int(user_y)]][cor_dict[int(user_x)]] = '.'
            print(cor_print(cor))

        elif int(user_x) <= 0:
            cor[cor_dict_y[int(user_y)]][cor_dict[int(user_x)]] = '.'
            print(cor_print(cor))

""" Save All Records """
def savefile():
    textfile = open("Your_coordinates.txt", "w")
    save_file = open("ForTheProgramOnly.txt", "w")
    textfile.write("Your coordinates : \n")

    for i in cor:
        save_file.write(" ".join(i))
        save_file.write("\n")
        if i == cor[5]:
            textfile.write(" ".join(i))
        else:
            textfile.write("  ".join(i[:5]) + " " + str(i[5]) + " " + "  ".join(i[6:]))
        textfile.write("\n")
    save_file.close()
    textfile.close()
    print("File Saved In The Same Directory")

""" OPENING LAST SAVE """

def openfile():
    print("NOTE : You Can Only Read your save but YOU CANNOT EDIT IT")
    file_open = open("ForTheProgramOnly.txt", "r")
    print(file_open.read())
    file_open.close()

# Original Program Starts From Here
while True:
    command = input("Command > ")

    if command == "add":
        add_point()

    elif command == "exit" or command == "quit" or command == "close":
        quit()

    elif command == "help":
        print("\n")
        print("add = for adding points")
        print("exit / quit / close = for quiting the program")
        print("clear = To Clear a Point")
        print("save = To save your coordinates")
        print("cls = To Clear the screen")
        print("open = To Open Your Last Save")
        print("Print = To print current coordinates again")
        print("\n")

    elif command == "clear":
        clear()

    elif command == "save":
        savefile()

    elif command == "print":
        print("\n")
        cor_print(cor)
        print("\n")

    elif command == "cls":
        os.system('cls')

    elif command == "open":
        openfile()

    else:
        print("Invalid Command")