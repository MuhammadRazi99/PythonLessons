def remainingCandy(caseNo):
    valueList=list(map(int,(input().split(' '))))
    candiesNo=sum(map(int,(input().split(' '))))
    return(f"Case #{caseNo}: {candiesNo%valueList[1]}")
testcase=int(input())
outputList=[]
for i in range(0,testcase):
    outputList.append(remainingCandy(i+1))
for i in range(testcase):
    print(outputList[i])
