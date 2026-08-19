import random
options=["rock", "paper", "scissors"]
user_wins=0
comp_wins=0
while True:
    user_choice=input("enter your choice::")
    if user_choice=="q":
        break
    index=random.randint(0,2)
    comp_choice=options[index]
    if comp_choice=="rock" and user_choice=="paper":
        print(comp_choice)
        print("YOU WIN!!!")
        user_wins+=1
    if comp_choice=="rock" and user_choice=="scissors":
        print(comp_choice)
        print("SORRY, YOU LOST")
        comp_wins+=1
    if comp_choice=="paper" and user_choice=="scissors":
        print(comp_choice)
        print("YOU WIN!!!")
        user_wins+=1
    if comp_choice=="paper" and user_choice=="rock":
        print(comp_choice)
        print("SORRY, YOU LOST")
        comp_wins+=1
    if comp_choice=="scissors" and user_choice=="rock":
        print(comp_choice)
        print("YOU WIN!!!")
        user_wins+=1
    if comp_choice=="scissors" and user_choice=="paper":
        print(comp_choice)
        print("SORRY, YOU LOST")
        comp_wins+=1
    if comp_choice==user_choice:
        print(comp_choice)
        print("TIE")
        continue
print("user wins=", user_wins)
print("computer wins=", comp_wins)


    
