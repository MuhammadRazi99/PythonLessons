def function(N, AlphaString, M, Keys):
    i = Keys.index(AlphaString[0])
    time = 0
    for a in range(1, N):
        j = Keys.index(AlphaString[a])
        time += abs(j - i)
        i = j
    return time


outputStr = []
testCase = int(input())
for _ in range(testCase):
    N = int(input())
    AlphaString = list(map(int, (input().split(' '))))
    M = int(input())
    Keys = list(map(int, (input().split(' '))))
    outputStr.append(function(N, AlphaString, M, Keys))

for i in range(testCase):
    print(f"Case #{i + 1}: {outputStr[i]}")
