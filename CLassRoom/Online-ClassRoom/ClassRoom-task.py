# O module is a file containing python code.
# fh = open("test.txt" ,'at')
# fh.write("This is a test")
# fh.write("This is a test")
# fh.write("'a',This is a test")
# fh.close()

# os.path.exists

# import os

# file_name = "test.txt"

# if os.path.exists(file_name):
#     print("File exists")
# else:
#     print("File does not exist")    

# pathlib module 
# from pathlib import Path
# file_name = Path('C:\\Users\\mrgus\\Desktop\\Python_Project\\test.txt')

# if file_name.exists():
#     print("File exists")
# else:
# print("File does not exist")
#     fh = open("test.txt" ,'at')
#     fh.write("This is a test")
#     fh.write("This is a test")
#     fh.write("'a',This is a test")
#     fh.close()


# common issue 
# fh = open("test.txt" ,'at')
# contents = fh.read()
# print(contents)


import random 

move = ["rock","paper","scissor"]
computer_move = random.choice(move)
keep_Playing = True

while keep_Playing:
    user_move = input("Enter your move: ")
    if user_move in move:
        if user_move == computer_move:
            print("Tie")
        elif user_move == "rock" and computer_move == "scissor":
            print("You win")
        elif user_move == "paper" and computer_move == "rock":
            print("You win")
        elif user_move == "scissor" and computer_move == "paper":
            print("You win")
        else:
            print("You lose")
        keep_Playing = False    
    else: 
        print("Invalid move")
        keep_Playing = False

