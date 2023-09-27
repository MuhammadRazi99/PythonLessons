class Domen:
    StaminaConsume=0
    
def Score(Doman):
    # frag=Demon[4][0:-1]
    sum=0
    turn=min(TurnsNo,len(Demon[4]))
    print(sum(Demon[4][:turn]))     
def StaminaRange(Stamina):
    if (Stamina in range(0,Maxstamina)):
        return Stamina
    elif(Stamina>Maxstamina):
        return Maxstamina
    else:
        return 0
        
with open("Reply/2022/input/00-example.txt","r") as file:
    line1 = list(map(int,file.readline().split()))
    global Currrentstamina,Maxstamina,TurnsNo,Demon
    Currrentstamina=line1[0]
    Maxstamina=line1[1]
    TurnsNo=line1[2]
    DemonsNo=line1[3]
    for _ in range(DemonsNo):
        line = list(map(int,file.readline().split()))
        d=line[0:4]
        d.append(list(line[4:]))
        Demon.append(d)
print(Demon)
print(Score(Demon[1]))
