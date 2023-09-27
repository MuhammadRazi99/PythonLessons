import random
def check(a,b):
    if a == "Rock" and b == "Paper":
        print("Winner: Player") 
    elif a == "Rock" and b == "Scissors":
        print("Winner: Computer")
    elif a == "Paper" and b == "Rock":
        print("Winner: Computer")
    elif a == "Paper" and b == "Scissors":
        print("Winner: Player") 
    elif a == "Scissors" and b == "Paper":
        print("Winner: Computer") 
    elif a == "Scissors" and b == "Rock":
        print("Winner: Player")
    else:
        print("Tie")  

l={"r":"Rock","p":"Paper","s":"Scissors"}
computer=random.choice(list(l.values()))
player=input('''"r":"Rock","p":"Paper","s":"Scissors"\nEnter the choice:''')
player=l.get(player)
print("Computer:",computer)
print("Player=",player)
check(computer,player)