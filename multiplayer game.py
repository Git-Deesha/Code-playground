import random
print("\t\t\tWELCOME TO THE MULTIPLAYER GAME!!!!\n")
def roll():
    roll=random.randint(1,6)
    return roll
while True:
    players=int(input("enter number of players ( 2 - 4 ):"))
    if 2<=players<=4:
        break
    else:
        print("enter suitable number of players")
max_score=20
p_score=0
p_names=[]
score=[]
for i in range(1,players+1):
    p_names.append(str(i))
while p_score<=max_score:
    for player in p_names:
        print("Player", player, "'s turn has started now\n")
        while True:
            value=roll()
            if value==1:
                print("You rolled a 1!! Your turn is complete\n\n")
                score.append(p_score)
                p_score=0
                break
            else:
                p_score+=value
                print("You rolled a  ", value )
            if p_score>=max_score:
                score.append(p_score)
                print("Your score is:",p_score,"\n\n")
                p_score=0
                break
    break
win_score=max(score)
winner=score.index(win_score)+1
print("Player", winner, "is the winner with a total score of:",win_score)

    
