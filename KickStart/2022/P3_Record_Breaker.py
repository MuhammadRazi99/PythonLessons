def function():
    M=int(input())
    V=list(map(int,input().split(' ')))
    count=0
    max=V[0]
    for i in range(0,M):
        if (i == 0 or V[i] > max) and ((i == M - 1) or V[i] > V[i + 1]): 
            count+=1
        if (max < V[i]):
            max = V[i]
    return count

def main():
  # Get number of test cases
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    print("Case #%d: %d" % (test_case, function()))


if __name__ == "__main__":
  main()
