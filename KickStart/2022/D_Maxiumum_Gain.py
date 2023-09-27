def function(N,N_list,M, M_list, question):
    max(N_list)

outputStr = []
testCase = int(input())
for _ in range(testCase):
    N=int(input())
    N_list = list(map(int, (input().split(' '))))
    M=int(input())
    M_list = list(map(int, (input().split(' '))))
    question=int(input())
    outputStr.append(function(N,N_list,M, M_list, question))

for i in range(testCase):
    print(f"Case #{i + 1}: {outputStr[i]}")
