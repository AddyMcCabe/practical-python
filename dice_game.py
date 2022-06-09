import random

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total


player1 = input("Enter player 1's name: ")
player2 = input("Enter player 2's name: ")

roll_1 = roll_dice()
roll_2 = roll_dice()

print(player1, "rolled", roll_1)
print(player2, "rolled", roll_2)

if roll_1 > roll_2:
    print(player1, "wins")
elif roll_1 == roll_2:
    print("It's a tie")
else:
    print(player2, "wins")