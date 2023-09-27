def decimalToBinary(n):
    return bin(n).replace("0b", "")
def minimumComplains(caseNo,valueList):    
    friendCoffee=[]
    invalidCoffee=[]
    mini=valueList[2]*valueList[0]
    for i in range(0,valueList[0]):
        friendCoffee.append(input())
    for i in range(0,valueList[1]):
        invalidCoffee.append(input())
    for coffee in range(0,2**valueList[2]):
        coffeetype=decimalToBinary(coffee)
        complain=0
        if(coffeetype in invalidCoffee):
            continue
        for friend in friendCoffee:
            for i in range(0,len(coffeetype)):
                if(coffeetype[i] != friend[i]):
                    complain=complain+1
        print(complain)
        if(complain<mini):
            mini=complain
    return f"Case #{caseNo}: {mini}"
testcase=int(input())
outputList=[]
for i in range(0,testcase):
    valueList=list(map(int,input().split(" ")))
    outputList.append(minimumComplains(i+1,valueList))
for i in range(0,testcase):
    print(outputList[i])