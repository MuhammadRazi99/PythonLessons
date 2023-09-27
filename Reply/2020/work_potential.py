import numpy as np
developer=[]
manager=[]
def bonusPotential(emp1,emp2):
    if(emp1[0]==emp2[0]):
        return int(emp1[1])*int(emp2[1])
    else:
        return 0
def workPotential(emp1,emp2):
    if(emp1[2]==None or emp2[2]==None):
        return 0
    else:
        commonSkills=[]
        nonCommonSkills=[]
        for i in range(int(emp1[2])):
            if(emp1[2+i] in emp2):
                commonSkills.append(emp1[2+i])
            else:
                nonCommonSkills.append(emp1[2+i])
        for i in range(int(emp2[2])):
            if(emp2[i+2] not in commonSkills):
                nonCommonSkills.append(emp2[2+i])
        return len(commonSkills)*len(nonCommonSkills)
def getEmployee(empNo):
    if("M" in empNo):
        empNo=int(empNo.replace("M",""))
        return manager[empNo]
    else:
        empNo=int(empNo.replace("_",""))
        return developer[empNo]
def findingPotential(room,row,col):
    potential=0
    for i in range(row):
        for j in range(col):
            if("M" in room[row][col] or "_" in room[row][col]):
                if(room[row][col-1]==None or room[row][col-1]==None):
                    pass
                elif("M" in room[row][col-1] or "_" in room[row][col-1]):
                    emp1=getEmployee(room[row][col])
                    emp2=getEmployee(room[row][col-1])
                    potential=potential+(bonusPotential(emp1,emp2))
                    potential=potential+(workPotential(emp1,emp2))
                else:
                    pass
                if(room[row-1][col]==None or room[row-1][col]==None):
                    continue
                elif(room[row-1][col]=="M   " or room[row-1][col]=="_   "):
                    emp1=getEmployee(room[row][col])
                    emp2=getEmployee(room[row-1][col])
                    potential=potential+(bonusPotential(emp1,emp2))
                    potential=potential+(workPotential(emp1,emp2))
                else:
                    pass
def getCordinates(room,empNo):
    r,w=room.where(empNo)
    return r,w
def outputFile(room,developerNo,managerNo):
    with open("Reply/2020/input/a_solar1.txt","w") as file:    
        for no in range(developerNo):
            pass

with open("Reply/2020/input/a_solar.txt","r") as file:
    line1 = list(map(int,file.readline().split()))
    row=line1[0]
    col=line1[1]  
    room=np.array([["0000"]*row]*col)
    for i in range(col):
        line = list(file.readline())
        for j in range(row):
            room[i][j]=line[j]+"   "
    developerNo=int(file.readline())
    for _ in range(developerNo):
        line = list(file.readline().split())
        developer.append(line)
    managerNo=int(file.readline())
    for _ in range(managerNo):
        line = list(file.readline().split())
        manager.append(line)

