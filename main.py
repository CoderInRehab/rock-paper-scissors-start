import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

img = [rock,paper,scissors]


user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

comp_choice = random.randint(0,2)

if user_choice > 2 or user_choice < 0:
  print("You typed an invalid number, you lose")
else:
  print(img[user_choice])

  print("Computer chose:")

  print(img[comp_choice])

  # if user_choice == comp_choice:
  #   print("It\'s a draw'")

  # else:
  #   if user_choice == 0:
  #     if comp_choice == 1:
  #       print("You lose")
  #     else:
  #       print("You win")
  #   if user_choice == 1:
  #     if comp_choice == 2:
  #       print("You lose")
  #     else:
  #       print("You win")
  #   if user_choice == 2:
  #     if comp_choice == 0:
  #       print("You lose")
  #     else:
  #       print("You win")

  if user_choice == 0 and comp_choice == 2: # 0 beats 2
    print("You win!")
  elif user_choice == 2 and comp_choice == 0: # 0 beats 2
    print("You lose!")
  elif comp_choice > user_choice: # 1 beats 0, 2 beats 1
    print("You lose")
  elif comp_choice < user_choice: # 0 beated by 1, 1 beated by 2
    print("You win!")
  elif comp_choice == user_choice: # 1 beats 0, 2 beats 1
    print("It's a Draw")
