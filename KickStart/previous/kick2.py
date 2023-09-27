def WhoWillRule(caseNo):
    kingdomName=input()
    RulerName=""
    if(kingdomName[-1]=='y'or kingdomName[-1]=='Y'):
        RulerName="nobody"
    elif(kingdomName[-1] in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']):
        RulerName="Alice"
    else:
        RulerName="Bob"
    return(f"Case #{caseNo}: {kingdomName} is ruled by {RulerName}.")
testcase=int(input())
outputList=[]
for i in range(0,testcase):
    outputList.append(WhoWillRule(i+1))
for i in range(testcase):
    print(outputList[i])
