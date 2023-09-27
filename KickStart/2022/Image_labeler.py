import statistics
from itertools import chain, combinations


def powerset(iterable,k):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)  # allows duplicate elements
    return chain.from_iterable(combinations(s, r) for r in range(k+1))

import statistics
def function(N, M):
    Region = list(map(int, (input().split(' '))))
    sol1=float(0)
    for i in range(1, M + 1):
        temp = []
        for j in range(0, len(Region), M-1):
            temp.append(Region[j])
        sol1 += statistics.median(temp)
    Region.sort()
    sol2 = float(0)
    for i in range(1, M+1):
        temp = []
        for j in range(0, len(Region), M-1):
            temp.append(Region[j])
        sol2 += statistics.median(temp)
    return max(sol1 , sol2)


outputStr = []
testCase = int(input())
for _ in range(testCase):
    N, M = map(int, (input().split(' ')))
    outputStr.append(function(N, M))

for i in range(testCase):
    print(f"Case #{i + 1}: {outputStr[i]}")
