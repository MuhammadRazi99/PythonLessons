import statistics
def function(N, M):
    Region = list(map(int, (input().split(' '))))
    Region.sort()
    sol = 0
    for i in range(1, M+1):
        temp = []
        for j in range(0, len(Region), M):
            print(Region[j])
            temp.append(Region[j])
        print(temp)
        sol += statistics.median(temp)
    return sol

print(function(3,2))