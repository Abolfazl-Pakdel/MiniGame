import random 

print("rock...")
print("paper...")
print("scissor...")
print("-------------------------")

randomNumber = random.randint(0, 2)
computerMove = "rock"

if randomNumber == 0:
  computerMove = "rock"
elif randomNumber == 1:
  computerMove = "paper"
elif randomNumber == 2:
  computerMove = "scissor"


Player_1 = input("Player_1 , Make your move : ")
Player_2 = computerMove
print(f"Player_2 , Make your move : {computerMove}")

if Player_1 == Player_2:
  print("THATS A TIE ....")
elif Player_1 == "rock":
  if Player_2 == "scissor":
    print("Player_1 Win!...")
  elif Player_2 == "paper":
    print("Player_2 Wins!...")
elif Player_1 == "paper":
  if Player_2 == "rock":
    print("Player_1 Win!...")
  elif Player_2 == "scissor":
    print("Player_2 Wins!...")
elif Player_1 == "scissor":
  if Player_2 == "paper":
    print("Player_1 Win!...")
  elif Player_2 == "rock":
    print("Player_2 Wins!...")
else:
  print("something went wrong!...")


"""
#-----------------------------------------------
if Player_1 == "rock" and Player_2 == "scissor":
  print("Player_1 Win!...")
elif Player_1 =="rock" and Player_2 == "paper":
  print("Player_2 Wins!...")
elif Player_1 =="paper" and Player_2 == "rock":
  print("Player_1 Wins!...")
elif Player_1 =="paper" and Player_2 == "scissor":
  print("Player_2 Wins!...")
elif Player_1 =="scissor" and Player_2 == "paper":
  print("Player_1 Wins!...")
elif Player_1 =="scissor" and Player_2 == "rock":
  print("Player_2 Wins!...")
elif Player_1 == Player_2:
  print("Thats a tie ...")
else:
  print("Something Went wrong ...")

"""