import random


def displayed_result(x):
    result = ""
    positions = []
    i = 0
    while i < len(x):
        if i % 3 == 0 and i != 0:
            result = result[:-1]
            result += "\n"
        if x[i] == 0:
            result += " -"
            positions.append(0)
        elif x[i] == 1:
            result += "X-"
            positions.append(1)
        else:
            result += "O-"
            positions.append(2)
        i += 1
    printed_result = result[:-1]
    print(printed_result)


def computer_logic(x):
    print("It's the computer's turn")
    string1 = "Please enter in which row you want to position the X: "
    print(string1, end="")
    string2 = "Please Enter in which column you want to position the X(choose from 1 to 3):"
    while True:
        row, column = random.randint(1, 3), random.randint(1, 3)
        new_position = (row - 1) * 3 + (column - 1)
        if x[new_position] != 1 and x[new_position] != 2:
            print(row)
            print(string2, end="")
            print(column)
            print(f"The computer chose row {row} and column {column} successfully.")
            print("New table will be\n")
            x[new_position] = 2
            displayed_result(x)
            break


def game_logic(s):
    while True:
        x = choice()
        new_position = (int(x[0]) - 1) * 3 + (int(x[2]) - 1)
        if s[new_position] == 1 or s[new_position] == 2:
            print("Sorry this position is already taken try again")
        else:
            s[new_position] = 1
            print(f"You chose row {x[0]} and column {x[2]} successfully.")
            print("New table will be\n")
            displayed_result(s)
            break


def choice():
    row_choice = input("Please enter in which row you want to position the X: ")

    while True:
        if row_choice == "exit":
            print("Hope you had fun")
            quit()
        elif row_choice == "end":
            main_game()
        elif 1 <= int(row_choice) <= 3:
            break
        else:
            print("Please enter the correct row.")
            row_choice = input("Please enter in which row you want to position the X(choose from 1 to 3)::")

    column_choice = input("Please Enter in which column you want to position the X(choose from 1 to 3):")

    while True:
        if column_choice == "exit":
            print("Hope you had fun")
            quit()
        elif column_choice == "end":
            main_game()
        elif 1 <= int(column_choice) <= 3:
            break
        else:
            print("Please enter the correct column.")
            column_choice = input("Please Enter in which column you want to position the X(choose from 1 to 3): ")

    position = row_choice + "-" + column_choice
    return position


def main_game():
    positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("""Welcome to the tic tak toe game.
The rules are you will first start the game by choosing where to position the X by choosing the row then column
after that the computer will choose where to position the O if you win a massage will be displayed to you informing you
of winning however if you lose you can play again also you can end the game whenever you want by typing end and exiting 
the whole game by typing exit.
Credits: Abdulaziz Alftaieh
If you face any problems you can contact me through my personal email: abdulaziz2661999@gmail.com
    """)
    name = input("Please enter your name:")
    while True:
        check_if_someone_won(positions, name)
        game_logic(positions)
        check_if_someone_won(positions, name)
        computer_logic(positions)
        check_if_someone_won(positions, name)


def check_if_someone_won(positions, name):

    player_array = [1, 1, 1]
    computer_array = [2, 2, 2]
    if positions[0:3] == player_array or positions[3:6] == player_array or positions[6:8] == player_array:
        print(f"{name} won!")
        quit()
    elif positions[0:3] == computer_array or positions[3:6] == computer_array or positions[6:8] == computer_array:
        print("Computer has won!")
        quit()
    elif (positions[0:9:4] == player_array) or (positions[2:7:2] == player_array):
        print(f"{name} won!")
        quit()
    elif (positions[0:9:4] == computer_array) or (positions[2:7:2] == computer_array):
        print("Computer has won!")
        quit()

    for i in range(0, len(positions) - 1):
        if positions[i:len(positions):3] == player_array:
            print(f"{name} won!")
            quit()
        elif positions[i:len(positions):3] == computer_array:
            print("Computer has won!")
            quit()
    if positions.count(0) == 0:
        print("It's a draw")
        quit()


main_game()
