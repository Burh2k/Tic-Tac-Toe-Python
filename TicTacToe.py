import tkinter as Tk
from tkinter import *
import random

root=Tk()
root.geometry("300x100")
root.title("Tic Tac Toe Game")

def cleargui():
    root.destroy()  
Button(root,text="Press Me to start yout game",font="Arial",command=cleargui).pack()
root.mainloop()
       
def end(tkin):    
    Label(tkin,text="Game Over",font="Arial").pack()


import random
Pattern = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}
New_Pattern = []

for key in Pattern:
    New_Pattern.append(key)

def printPattern(board):
    print(' _____________')
    print(' | '+board['1'] + ' | ' + board['2'] + ' | ' + board['3']+ ' |')
    print(' _____________')
    print(' | '+board['4'] + ' | ' + board['5'] + ' | ' + board['6']+' |')
    print(' _____________')
    print(' | '+board['7'] + ' | ' + board['8'] + ' | ' + board['9']+' |')
    print(' _____________')

player1=input("Player 1 : ")
player2=input("Player 2 : ")
ram=random.randint(1,10)
swap=""

def game():
    count = 0
    if (ram > 5):
        turn = player1
        swap = "1"
    else:
        turn = player2
        swap = "2"
    for i in range(10):
        printPattern(Pattern)
        move = input("Player " + swap +" Turn, Enter Location : ")
        if move == "":
            print(" --- Nothing was Entered --- ")
            continue
        elif Pattern[move] == ' ':
            Pattern[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            result=Tk()
            result.geometry("300x150")
            result.title("Game Result")
            if Pattern['7'] == Pattern['8'] == Pattern['9'] != ' ':  # across the top
                printPattern(Pattern)
                dis= "Player " + swap + "won."
                Button(result,text=dis,command=end(result)).pack()
                result.mainloop()
                break
            elif Pattern['4'] == Pattern['5'] == Pattern['6'] != ' ':  # across the middle
                printPattern(Pattern)
                dis= "Player " + swap + "won."
                Button(result,text=dis,command=end(result)).pack()
                result.mainloop()
                break
            elif Pattern['1'] == Pattern['2'] == Pattern['3'] != ' ':  # across the bottom
                printPattern(Pattern)
                dis= "Player " + swap + "won."
                Button(result,text=dis,command=end(result)).pack()
                result.mainloop()
                break
            elif Pattern['1'] == Pattern['4'] == Pattern['7'] != ' ':  # down the left side
                printPattern(Pattern)
                dis= "Player " + swap + "won."
                Button(result,text=dis,command=end(result)).pack()
                result.mainloop()
                break
            elif Pattern['2'] == Pattern['5'] == Pattern['8'] != ' ':  # down the middle
                printPattern(Pattern)
                dis= "Player " + swap + "won."
                Button(result,text=dis,command=end(result)).pack()
                result.mainloop()
                break
            elif Pattern['3'] == Pattern['6'] == Pattern['9'] != ' ':  # down the right side
                printPattern(Pattern)
                dis= "Player " + swap + "won."
                Button(result,text=dis,command=end(result)).pack()
                result.mainloop()
                break
            elif Pattern['7'] == Pattern['5'] == Pattern['3'] != ' ':  # diagonal
                printPattern(Pattern)
                dis= "Player " + swap + "won."
                Button(result,text=dis,command=end(result)).pack()
                result.mainloop()
                break
            elif Pattern['1'] == Pattern['5'] == Pattern['9'] != ' ':  # diagonal
                printPattern(Pattern)
                dis= "Player " + swap + "won."
                Button(result,text=dis,command=end(result)).pack()
                result.mainloop()
                break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if swap == "1":
            turn=player2
            swap = "2"
        else:
            swap="1"
            turn=player1

            # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in New_Pattern:
            Pattern[key] = " "

        game()
if __name__ == "__main__":
    game()