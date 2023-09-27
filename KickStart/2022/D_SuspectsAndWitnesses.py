from itertools import chain, combinations


def powerset(iterable,k):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)  # allows duplicate elements
    return chain.from_iterable(combinations(s, r) for r in range(k+1))


def function(N, M, K, W):
    suspect=[]
    for _ in range(1,N):
        suspect.append(0)
    list=powerset(N,K)
    for i in range(len(list)):



outputStr = []
testCase = int(input())
for _ in range(testCase):
    N, M, K = map(int, (input().split(' ')))
    WitnessStatement=[]
    for _ in range(0, M):
        temp=list(map(int, (input().split(' '))))
        WitnessStatement.append(temp)
        outputStr.append(function(N, M, K, WitnessStatement))

for i in range(testCase):
    print(f"Case #{i + 1}: {outputStr[i]}")
