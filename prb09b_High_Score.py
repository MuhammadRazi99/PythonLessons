def game():
    return 45450
score=game()
f=open("prb09b_High_Score.txt")
HighScore=f.readline()
f.close()
if HighScore=="":
    with open("prb09b_High_Score.txt","w") as f:
        f.write(str(score)+"\n")
elif int(HighScore)<score:
    with open("prb09b_High_Score.txt","a") as f:
        f.write(str(score)+"\n")
else:
    pass