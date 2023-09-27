import numpy as np
def no_of_box_needed(caseNo):
    CellStruct=list(map(int,input().split(' ')))
    cell=np.array([],ndim=2)
    for i in range(CellStruct[1]):
        rowValues=list(map(int,input().split(' ')))
        for j in range(CellStruct[0]):
            cell.append(rowValues[j])
    cell.ad
testcase=int(input())
outputList=[]
for i in range(0,testcase):
    outputList.append(no_of_box_needed(i+1))
for i in range(testcase):
    print(outputList[i])
