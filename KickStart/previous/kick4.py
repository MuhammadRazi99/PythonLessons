'''
Impossible: If it was impossible for two players to follow the rules and to have arrived at that game state.
Red wins: If the player playing the red stones has won.
Blue wins: If the player playing the blue stones has won.
Nobody wins: If nobody has yet won the game. Note that a game of Hex cannot end without a winner!
'''
import numpy


def GameState(caseNo):
    columnsNo=int(input())
    stage=list(map(int,(input().split(' '))))
    arr=numpy.array([],ndim=2)
    Blueflag=True  
    for i in range(columnsNo*columnsNo):
        arr.append(stage[i])
    if (stage.count('B')==stage.count('R')):
        pass
    for i in range(columnsNo):
        for j in range(columnsNo):
            if(arr[i][j] is not 'B'):
                Blueflag=False
                break
        if(Blueflag):
            return f"Case #{caseNo}: Blue wins"

    return f"Case #{caseNo}: Nobody wins"
testcase=int(input())
outputList=[]
for i in range(testcase):
    outputList.append(GameState(i+1))
for i in range(testcase):
    print(outputList[i])