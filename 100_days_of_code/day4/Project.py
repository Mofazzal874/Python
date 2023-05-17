#rock paper scissors game 


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

#Write your code below this line 👇
you = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Sciessors: "))
if you == 0:
    print(rock)
elif you == 1:
    print(paper)
elif you == 2:
    print(scissors)

computer = random.randint(0 , 2)
print(f"computer chose:{computer}\n") 

if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer == 2:
    print(scissors)


if you == 0 and computer == 1:
    print("you win")
elif computer == 0 and you == 0 :
    print("draw")
elif computer ==0 and you == 1:
    print("you win")
elif you == 1 and computer == 1 :
    print("draw") 
elif you == 1 and computer == 2:
    print("you lose")
elif you == 2 and computer ==2 :
    print("draw")
elif you ==2 and computer == 1:
    print("you win")


