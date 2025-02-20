import random

bot = random.choice([-1, 0, 1])
# print(bot)
player = input("Enter your choice (s/w/g): ")
selection = {
    "s" : -1,
    "w" : 0,
    "g" : 1
}
player = selection[player]

yourSelection = {
    -1 : "Snake",
    0 : "Water",
    1 : "Gun"
}
print("your selection is:", yourSelection[player])
print("Bot selection is:", yourSelection[bot])

print("\n ============Game Result============\n")

if player == bot:
    print("It's a tie")
    print("\n ============Game Over============\n")
    
    exit()
else:
    if player == -1:
        if bot == 0:
            print("You win")
        else:
            print("You lose")
    elif player == 0:
        if bot == 1:
            print("You win")
        else:
            print("You lose")
    else:
        if bot == -1:
            print("You win")
        else:
            print("You lose")
            
            
# Output:

print("\n ============Game Over============\n")