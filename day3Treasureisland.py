#This is a code using if else nesting tables to make a Treasure island game where a certain path leads to treasure
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************''')
print("Welcome to Treasure Island.\nYour mission is to find treasure")
if input('''You're at a cross road. Where do you want to go? Type "left" or "right"\n''').lower()=="right":
    print("You fell into a hole. Game Over")
else:
    if input('''You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for boat. Type "swim" to swim across.\n''').lower()=="swim":
        print("Your got attached by an angry trout. Game Over.")
    else:
        door=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").lower()
        if door=="yellow":
            print("You found Treasure! You win!")
        elif door=="red":
            print("It's a room full of fire. Game Over.")
        else:
            print("You entered a room full of beasts. Game Over.")