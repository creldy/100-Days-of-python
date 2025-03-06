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

index = [rock, paper, scissors]
comp_choice = random.randint(0,2)
user_choice= input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
print(index[int(user_choice)])
print("Computer chose:")
print(index[int(comp_choice)])

if comp_choice==int(user_choice):
    print("It is a draw.")
elif comp_choice==2 and int(user_choice)==0:
    print("You win!")
elif comp_choice==0 and int(user_choice)==2:
    print("You lose :(")
elif comp_choice>int(user_choice):
    print("You lose :(")
else:
    print("You win!")