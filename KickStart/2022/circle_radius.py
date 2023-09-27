import math
def calculateArea(r,a,b):
    Area=[]
    i=r
    area=math.pi*i*i
    Area.append(area)
    while(i!=0):
        i=i*a
        area=math.pi*i*i
        Area.append(area)
        i=int(i/b)
        area=math.pi*i*i
        Area.append(area)
    return str(sum(Area))


outputStr=[]
testCase=int(input())
for _ in range(testCase):
    values=list(map(int,(input().split(' '))))
    outputStr.append(calculateArea(values[0],values[1],values[2]))

for i in range(testCase):
    print(f"Case #{i+1}: {outputStr[i]}")