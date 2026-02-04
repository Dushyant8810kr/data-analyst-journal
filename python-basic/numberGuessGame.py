#Game 1 :-Guessing a number
"""import random

num = random.randint(1,100)

tries = 0
while True:
    guessed = int(input("Guess the number between (1-100) : "))
    tries +=1
    if guessed == num:
        print(f"you guessed the number in {tries} no. of tries")
        break
    elif guessed > num:
        print("sorry you need to go lower")
    elif guessed<num:
        print("sorry you need to go higher")"""


#Game 2 :- stone, paper , scissors game

"""import random


cscore = 0
uscore = 0

while True:
    user = int(input("1 for stone , 2 for paper , 3 for scissors : "))
    com = random.randint(1,3)

    if user == 1 and com == 3:
        uscore+=1
        print("You won this round")

    elif user == 2 and com == 1:
        uscore+=1
        print("You won this round")

    elif user == 3 and com == 2:
        uscore+=1
        print("You won this round")

    else:
        cscore+=1
        print("computer won this round")
    
    if uscore == 5:
        print("You won this round")
        break

    elif cscore == 5:
        print("computer won this round")
        break"""

#stone, paper , scissors game(with ui):-

"""import tkinter as tk
import random

# scores
cscore = 0
uscore = 0

def play(user):
    global cscore, uscore

    com = random.randint(1, 3)

    choices = {1: "Stone", 2: "Paper", 3: "Scissors"}

    user_choice.config(text=f"You chose: {choices[user]}")
    comp_choice.config(text=f"Computer chose: {choices[com]}")

    if user == 1 and com == 3:
        uscore += 1
        result.config(text="You won this round 🎉")

    elif user == 2 and com == 1:
        uscore += 1
        result.config(text="You won this round 🎉")

    elif user == 3 and com == 2:
        uscore += 1
        result.config(text="You won this round 🎉")

    else:
        cscore += 1
        result.config(text="Computer won this round 🤖")

    score.config(text=f"Score → You: {uscore} | Computer: {cscore}")

    if uscore == 5:
        result.config(text="🎉 YOU WON THE GAME 🎉")
        disable_buttons()

    elif cscore == 5:
        result.config(text="🤖 COMPUTER WON THE GAME 🤖")
        disable_buttons()

def disable_buttons():
    stone_btn.config(state="disabled")
    paper_btn.config(state="disabled")
    scissors_btn.config(state="disabled")

def reset_game():
    global cscore, uscore
    cscore = 0
    uscore = 0

    score.config(text="Score → You: 0 | Computer: 0")
    result.config(text="")
    user_choice.config(text="")
    comp_choice.config(text="")

    stone_btn.config(state="normal")
    paper_btn.config(state="normal")
    scissors_btn.config(state="normal")

# UI window
root = tk.Tk()
root.title("Stone Paper Scissors")
root.geometry("400x420")

tk.Label(root, text="Stone Paper Scissors", font=("Arial", 16, "bold")).pack(pady=10)

user_choice = tk.Label(root, text="", font=("Arial", 12))
user_choice.pack()

comp_choice = tk.Label(root, text="", font=("Arial", 12))
comp_choice.pack()

result = tk.Label(root, text="", font=("Arial", 12, "bold"))
result.pack(pady=10)

score = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Arial", 12))
score.pack(pady=10)

stone_btn = tk.Button(root, text="Stone", width=15, command=lambda: play(1))
stone_btn.pack(pady=5)

paper_btn = tk.Button(root, text="Paper", width=15, command=lambda: play(2))
paper_btn.pack(pady=5)

scissors_btn = tk.Button(root, text="Scissors", width=15, command=lambda: play(3))
scissors_btn.pack(pady=5)

reset_btn = tk.Button(root, text="Reset Game", width=15, command=reset_game)
reset_btn.pack(pady=15)

root.mainloop() """