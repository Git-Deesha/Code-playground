import random
top=int(input("enter top number"))
num=random.randint(0,top)
guess=1
while True:
    gnum=int(input("enter your guess"))
    if gnum>num:
        print("guess lower")
        guess+=1
    elif gnum<num:
        print("guess higher")
        guess+=1
    elif gnum==num:
        print("you guessed the number right in:", guess, end=" guesses")
        print()
        break
