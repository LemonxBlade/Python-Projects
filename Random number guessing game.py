#Random number gussing game by LemonXBlade
import random

#Logic
flag = True
while flag:
    num = input("Type number upper bound: ")

    if num.isdigit():
        print("Lets`s Play!")
        num = int(num)
        flag = False
    else:
        print("Invaild Input! Try Again Bro")

# Main Game

secret = random.randint(1,num)

guess = None
count = 1

while guess != secret:
    #guess = input('Please type a number between 1 & ' + str(num)":")~ why dose this line not work!
    guess = input("Enter Numer between 1 and " + str(num) + ': ' )
    if guess.isdigit():
        guess = int(guess)

    if guess == secret:
        print("Well done!")
    else:
        print("Try Again!")
        count += 1

print("It took you ", count ,"gueeses! to guess Right WoW!")

