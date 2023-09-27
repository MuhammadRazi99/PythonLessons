import random
computer=random.randint(1,100)
user=int(input("Enter a number="))
tries=1
while(computer!=user):
    if computer>user:
        print("Guess wrong.Enter a Bigger no.")
        user=int(input(">>>")) 
    else:
        print("Guess wrong.Enter a Smaller no.")
        user=int(input(">>>"))
    tries+=1
highScore=[0,0,0]
with open("Project2_HighScore.txt") as f:
    for i in range(0,3): 
        a=f.readline()
        highScore[i]=int(a)

if tries<highScore[2]:
    print("High Score")
    highScore[i]=tries
    highScore.sort()
else:
    exit()
with open("Project2_HighScore.txt","w") as f:
    for i in range(0,3):
        if i!=2:
            f.write(str(highScore[i])+"\n")
        else:        
            f.write(str(highScore[i]))

print(f"You win after {tries} tries")