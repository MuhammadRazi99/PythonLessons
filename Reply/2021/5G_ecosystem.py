import numpy as np
def latencyWeight(e):
    return e[3]
def distance(a,b):
    pass
def antennaPlace(city,element,x,y):
    row,col=np.shape(city)
    for i in range(0,element[1]+1):
        for j in range(0,element[1]-i+1):
            if((x+i)>row or (y+j)>col):
                pass
            elif (city[x+i][y+j][0]=='B'):
                city[x+i][y+j]=city[x+i][y+j]+"A"+element[0]+" "+element[2]
            else:
                city[x+i][y+j]=f"A{element[0]} {element[2]}   "
            if((x-i)<0 or (y+j)>col):
                pass
            elif (city[x-i][y+j][0]=='B'):
                city[x-i][y+j]=city[x-i][y+j]+"A"+str(element[0])+" "+str(element[2])
            else:
                city[x-i][y+j]=f"A{element[0]} {element[2]}   "
        for j in range(0,element[1]-i+1):
            if((x+i)>row or (y-j)<0):
                pass
            elif (city[x+i][y-j][0]=='B'):
                city[x+i][y-j]=city[x+i][y-j]+"A"+str(element[0])+" "+str(element[2])
            else:
                city[x+i][y-j]=f"A{element[0]} {element[2]}   "
            if((x-i)<0 or (y-j)<0):
                pass
            elif (city[x-i][y-j][0]=='B'):
                city[x-i][y-j]=city[x-i][y-j]+"A"+element[0]+" "+element[2]
            else:
                city[x-i][y-j]=f"A{element[0]} {element[2]}   "
    return city

with open("Reply/input/data_scenarios_a_example.in","r") as file:
    line1 = list(map(int,file.readline().split()))
    city=np.array([["NA     "]*line1[1]]*line1[0])
    line2=list(map(int,file.readline().split()))
    buildingNo=line2[0]
    antennaNo=line2[1]
    rewardNo=line2[2]
    buildingList=[]
    antennaList=[]
    for _ in range(buildingNo):
        build=list(map(int,file.readline().split()))
        buildingList.append(build)
        city[build[0]][build[1]]=f"B{build[2]+1}     "
    for _ in range(antennaNo):
        antenna=list(map(int,file.readline().split()))
        antenna.insert(0,_)
        antennaList.append(antenna)
buildingList.sort(reverse=True,key=latencyWeight)
# print(antennaList)
print(city)
element=[1,2,2]
city2=antennaPlace(city,element,10,7)
print(city2)