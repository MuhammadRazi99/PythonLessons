import math
def isPalindrome(s):
    return s == s[::-1]
def palindrome_factor(no):
    count=0
    if(isPalindrome(str(no))):
        count+=1
    for i in range(1,int(no/2)+1):
        if(no%i==0):
            if(isPalindrome(str(i))):
                count+=1
    return count
outputStr=[]
testCase=int(input())
for _ in range(testCase):
    no=int(input())
    outputStr.append(palindrome_factor(no))

for i in range(testCase):
    print(f"Case #{i+1}: {outputStr[i]}")