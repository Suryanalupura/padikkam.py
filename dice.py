import random
while True:
    dice = input("Would you like to roll the dice (yes='y'/no='n'): ")
    if dice == "y":
        n = random.randint(1,6)
        print("Value on the dice is " + str(n))
        if n == 1:
            print(" _______")
            print("|       |")
            print("|       |")
            print("|   o   |")
            print("|       |")
            print("|_______|")
        elif n == 2:
            print(" _______")
            print("|       |")
            print("|   o   |")
            print("|       |")
            print("|   o   |")
            print("|_______|")
        elif n == 3:
            print(" _______")
            print("|       |")
            print("|   o   |")
            print("|   o   |")
            print("|   o   |")
            print("|_______|")
        elif n == 4:
            print(" _______")
            print("|       |")
            print("| o   o |")
            print("|       |")
            print("| o   o |")
            print("|_______|")
        elif n == 5:
            print(" _______")
            print("|       |")
            print("| o   o |")
            print("|   o   |")
            print("| o   o |")
            print("|_______|")
        else:
            print(" _______")
            print("|       |")
            print("| o   o |")
            print("| o   o |")
            print("| o   o |")
            print("|_______|")
    elif dice == "n":
        break;
    else:
        print("Invalid command")
