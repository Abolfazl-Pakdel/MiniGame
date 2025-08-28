import random 
import termcolor
import termcolor2
import pyfiglet

print(termcolor2.colored("Wellcome to RPS Game", "green"))
print(termcolor2.colored("Produced by APP Programmer", "red"))

player_1_count_win = 0
player_2_count_win = 0
computer_count_win = 0
player_count_win = 0
number_of_Game = 0

com = random.randint(0, 2)
computer_move = ""

if com == 0:
  computer_move = "rock"
elif com == 1:
  computer_move = "scissor"
elif com == 2:
  computer_move = "paper"

while True:
  print(termcolor2.colored("chose bettwen 1 to 3", "dark_grey"))
  print(termcolor2.colored("1. Play with Bot", "yellow"))
  print(termcolor2.colored("2. Play with friend", "yellow"))
  print(termcolor2.colored("3. EXIT",  "yellow"))
  first_input = int(input("=>"))
  if first_input == 3:
    break
# =-----------------------------
  elif first_input == 1:
    while player_count_win < 3 and computer_count_win < 3:
      print(f"the scors until now\n player : {player_count_win} | computer : {computer_count_win}")
      humen = input("Enter your Move!! => ")
      if humen == computer_move:
        print(termcolor2.colored("!!! DRAW !!!", "red"))
      elif humen == "rock":
        if computer_move == "scissor":
          print(termcolor2.colored("!!! WINS Good job!!!", "blue"))
          player_count_win += 1
          number_of_Game += 1
        elif computer_move == "paper":
          print(termcolor2.colored("computer WINS!!!", "blue"))
          computer_count_win += 1
          number_of_Game += 1
      elif humen == "paper":
        if computer_move == "rock":
          print(termcolor2.colored("!!! WINS Good job!!!", "blue"))
          player_count_win += 1
          number_of_Game += 1
        elif computer_move == "scissor":
          print(termcolor2.colored("computer WINS!!!", "blue"))
          computer_count_win += 1
          number_of_Game += 1
      elif humen == "scissor":
        if computer_move == "paper":
          print(termcolor2.colored("!!! WINS Good job!!!", "blue"))
          player_count_win += 1
          number_of_Game += 1
        elif computer_move == "rock":
          print(termcolor2.colored("computer WINS!!!", "blue"))
          computer_count_win += 1
          number_of_Game += 1
#----------------------------------------------- 
  elif first_input == 2:
    while number_of_Game < 3:
      print(f"the scors until now\n player_1 : {player_1_count_win} | player_2 : {player_2_count_win}")
      player_1 = input("Player_1 Move!! => ")
      player_2 = input("Player_2 Move!! => ")

      if player_1 == player_2:
        print(termcolor2.colored("!!! DRAW !!!", "red"))
      elif player_1 == "rock":
        if player_2 == "scissor":
          print(termcolor2.colored("Player_1 WINS!!!", "blue"))
          player_1_count_win += 1
          number_of_Game += 1
        elif player_2 == "paper":
          print(termcolor2.colored("player_2 WINS!!!", "blue"))
          player_2_count_win += 1
          number_of_Game += 1
      elif player_1 == "paper":
        if player_2 == "rock":
          print(termcolor2.colored("Player_1 WINS!!!", "blue"))
          player_1_count_win += 1
          number_of_Game += 1
        elif player_2 == "scissor":
          print(termcolor2.colored("player_2 WINS!!!", "blue"))
          player_2_count_win += 1
          number_of_Game += 1
      elif player_1 == "scissor":
        if player_2 == "paper":
          print(termcolor2.colored("Player_1 WINS!!!", "blue"))
          player_1_count_win += 1
          number_of_Game += 1
        elif player_2 == "rock":
          print(termcolor2.colored("player_2 WINS!!!", "blue")) 
          player_2_count_win += 1
          number_of_Game += 1 


"""
# single player logic
humen = input("Enter your Move!!")

if humen == computer_move:
  print(termcolor2.colored("!!! DRAW !!!", "red"))
elif humen == "rock":
  if computer_move == "scissor":
    print(termcolor2.colored("!!! WINS Good job!!!", "blue"))
  elif computer_move == "paper":
    print(termcolor2.colored("computer WINS!!!", "blue"))
elif humen == "paper":
  if computer_move == "rock":
    print(termcolor2.colored("!!! WINS Good job!!!", "blue"))
  elif computer_move == "scissor":
    print(termcolor2.colored("computer WINS!!!", "blue"))
elif humen == "scissor":
  if computer_move == "paper":
    print(termcolor2.colored("!!! WINS Good job!!!", "blue"))
  elif computer_move == "rock":
    print(termcolor2.colored("computer WINS!!!", "blue"))



# to player logic
player_1 = input("Player_1 Move!! => ")
player_2 = input("Player_2 Move!! => ")

if player_1 == player_2:
  print(termcolor2.colored("!!! DRAW !!!", "red"))
elif player_1 == "rock":
  if player_2 == "scissor":
    print(termcolor2.colored("Player_1 WINS!!!", "blue"))
  elif player_2 == "paper":
    print(termcolor2.colored("player_2 WINS!!!", "blue"))
elif player_1 == "paper":
  if player_2 == "rock":
    print(termcolor2.colored("Player_1 WINS!!!", "blue"))
  elif player_2 == "scissor":
    print(termcolor2.colored("player_2 WINS!!!", "blue"))
elif player_1 == "scissor":
  if player_2 == "paper":
    print(termcolor2.colored("Player_1 WINS!!!", "blue"))
  elif player_2 == "rock":
    print(termcolor2.colored("player_2 WINS!!!", "blue"))  
"""