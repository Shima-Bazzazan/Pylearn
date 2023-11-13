
import datetime
import random
import pyfiglet
from colorama import Fore


def menu():
    tittle = pyfiglet.figlet_format("Tic Tac Toe", font = "slant")
    print(tittle)
    print("Choose one of the following two modes:")
    print("1. Player VS Cpu")
    print("2. Player VS Player")


def game_mode():
    user_choice = int(input())
    return user_choice


def show_board():
    for row in game_board:
        for cell in row:
            if cell == "X":
                print(Fore.RED + "X", end = " ")
            elif cell == "O":
                print(Fore.BLUE + "O", end = " ")
            else:
                print(Fore.RESET + cell, end = " ")
        print(Fore.RESET)


def get_input(role: str, temp: str):
    while True:
        print(f"\n{role}")

        if role == "Cpu":
           
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if game_board[row][col] == "-":
                game_board[row][col] = temp
                print("row:", row + 1)
                print("col:", col + 1)
                break
        else:
            row = int(input("row (1 - 3): "))
            col = int(input("col (1 - 3): "))

            if 1 <= row <= 3 and 1 <= col <= 3:
                if game_board[row - 1][col - 1] == "-":
                    game_board[row - 1][col - 1] = temp
                    break
                else:
                    print("This cell is filled! Please try again.")
            else:
                print("Row and Column must be between (1,3)!")
            

def check_game(role: str, temp: str, startTime: int):
    if check_win(temp) == True:
        print(f"\n{role} wins!")
        endTime = datetime.datetime.now().replace(microsecond =0 )
        print("Game Duration:", endTime - startTime)
        exit()
    else:
        if check_draw() == True:
            print("\nDraw!")
            endTime = datetime.datetime.now().replace(microsecond = 0)
            print("Game Duration:", endTime - startTime)
            exit()
            
            
def check_win(temp: str):
    win = False

    for i in range(3):
        if (game_board[i][0] == game_board[i][1] == game_board[i][2] == temp) or (game_board[0][i] == game_board[1][i] == game_board[2][i] == temp):
            win = True
            break
    if (game_board[0][0] == game_board[1][1] == game_board[2][2] == temp) or (game_board[0][2] == game_board[1][1] == game_board[2][0] == temp):
        win = True
    
    return win


def check_draw():
    if not any("-" in i for i in game_board):
        return True
    else:
        return False


def game_play(user_choice: int):
    show_board()
    startTime = datetime.datetime.now().replace(microsecond = 0)

    if user_choice == 1:
        while True:
            get_input("Player", "X")
            show_board()
            check_game("Player", "X", startTime)
            
            get_input("Cpu", "O")
            show_board()
            check_game("Cpu", "O", startTime)

    elif user_choice == 2:
        while True:
            get_input("Player1", "X")
            show_board()
            check_game("Player1", "X", startTime)

            get_input("Player2", "O")
            show_board()
            check_game("Player2", "O", startTime)

    else:
        while True:
            print("The input is not valid!")
            choice = game_mode()

            if user_choice == 1:
                break
            elif user_choice == 2:
                break
            
        game_play(user_choice)
               

game_board = [["-", "-", "-"],
             ["-", "-", "-"],
             ["-", "-", "-"]]

menu()
game_play(game_mode())
