def function():
    N,R,C,Sr,Sc=list(map(int,input().split(' ')))
    moves=input()
    stepmarks=[]
    stepmarks.append((Sr,Sc))
    for i in range(0,len(moves)):    
        
        if moves[i] == 'E':
            Sc+=1
        elif moves[i] == 'W':
            Sc-=1
        elif moves[i] == 'N':
            Sr-=1
        elif moves[i] == 'S':
            Sr+=1
        
        if (Sr,Sc) in stepmarks:
            i=i-3
            continue
        else:
            stepmarks.append((Sr,Sc))
    
    print(stepmarks)
    ans=f"{Sr} {Sc}"
    return ans

def main():
  # Get number of test cases
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    print(f"Case #{test_case}: {function()}")

if __name__ == "__main__":
  main()
