def candyDistributor():
    (N,M)=map(int,(input().split(' ')))
    CandyList=list(map(int,(input().split(' '))))
    output=sum(CandyList)%M
    return str(output)

outputStr=[]
testCase=int(input())
for _ in range(testCase):
    outputStr.append(candyDistributor())

for i in range(testCase):
    print(f"Case #{i+1}: {outputStr[i]}")