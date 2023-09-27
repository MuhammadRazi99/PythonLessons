def HindexCalculator(caseNo):
    papersNo=int(input())
    outputString=f"Case #{caseNo}:"
    ol=[]
    citeList=list(map(int,(input().split(' '))))
    for i in range(0,papersNo):
        if ol:
            prev=ol[-1]
        else:
            prev=1
        if(ol.count(prev)>prev):
            prev=prev+1
        ol.append(prev)
    for value in ol:
        outputString=outputString+" "+str(value)
    return outputString+" "

testcase=int(input())
outputList=[]
for i in range(0,testcase):
    outputList.append(HindexCalculator(i+1))
for i in range(0,testcase):
    print(outputList[i])

    