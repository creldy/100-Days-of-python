print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
dirOne = input("Do you want to turn left or right?")
if dirOne == "Left" or "left":
    print("You've come to the lake. There is an island in the middle of the lake.")
    waitOrSwim =input("Do you want to wait for a boat or swim to the island?(wait/swim)")
    if waitOrSwim== "wait" or "wait":
        print("You arrive at the island unharmed and there are three doors.")
        door = input("One red, one yellow and one blue. Which colour door do you choose?(red/yello/blue)")
        if door== "Blur" or "blue":
            print("You were beaten by the beasts in the room. GAME OVER...")
        elif door=="Red" or "red":
            print("The poison gas inside the room has killed you. GAME OVER...")
        elif door=="Yellow" or "yellow":
            print("Yay! You have found the treasure!!!!!!!!")
        else:
            print("Invalid option. GAME OVER...")
    elif waitOrSwim=="Swim" or "swim":
        print("You have been eaten by the crocodile. GAME OVER...")
    else:
        print("Invalid option. GAME OVER...")
elif dirOne == "Right" or "right":
    print("You fell into a hole. GAME OVER...")
else:
    print("Invalid option. GAME OVER...")
