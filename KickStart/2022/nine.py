def check_nine(num):
    NS=str(num)
    NSList=list(map(int,NS))
    remaninder=sum(NSList)%9
    remaninder=9-remaninder
    if (remaninder==0):
        return num
    if(int(str(remaninder)+NS)>int(NS+str(remaninder))):
        return int(NS+str(remaninder))
    else:
        return int(str(remaninder)+NS)
    


outputStr=[]
testCase=int(input())
for _ in range(testCase):
    No=int(input())
    outputStr.append(check_nine(No))

for i in range(testCase):
    print(f"Case #{i+1}: {outputStr[i]}")