def buildingPalindromes(questionStr):
    middle=True
    if(len(questionStr)%2==0):
        middle=False
    return palindrome(questionStr,middle)
    
def palindrome(questionStr,middle):
    if (questionStr=='' or len(questionStr)==1):
        return True
    alpha=questionStr[0]
    questionStr=questionStr.replace(alpha,'',1)
    if(alpha in questionStr):
        questionStr=questionStr.replace(alpha,'',1)
        return palindrome(questionStr,middle)
    else:
        if(middle):
            middle=False
            questionStr=questionStr.replace(alpha,'',1)
            return palindrome(questionStr,middle)
        else:
            return False

def main():
  # Get number of test cases
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    # Get total of left and right parentheses
    N, Q = map(int, input().split())
    block=input()
    yesAnswer=0
    for i in range(Q):
        l,r=map(int,input().split())
        questionStr=block[l-1:r]
        ans = buildingPalindromes(questionStr)
        if(ans):
            yesAnswer+=1
    print("Case #%d: %d" % (test_case, yesAnswer))


if __name__ == "__main__":
  main()
