import random

print("lets play GUESSING GAME!")
print("Rules:")
print("1. The number should be between 0-100")
print("2. You get 5 chances to guess the number ")
print("Let's start the game !!", end="\n\n")
number=random.randint(0,100)
while(True):
    for i in range(3):
        guess=int(input(f"Enter your {i+1}th guess: "))
        if guess==number:
            print("you have guessed the correct number ",str(guess),end="\n")
            break
        else:
            print("you have guessed the wrong number",str(guess),end="\n")
    print("!!!!!!GAME OVER!!!!!!")
