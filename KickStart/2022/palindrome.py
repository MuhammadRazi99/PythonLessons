from dataclasses import replace
from operator import index


def isPalindrome(s):
    return s == s[::-1]
def convert_palindrome(No_len,No):
    counter=No.count("?")
    for i in range(counter):
        value=No[-int(index("?"))+1]
        replace("?",value)
    if(isPalindrome(No)):
        return "POSSIBLE"
    else:
        return "IMPOSSIBLE"

outputStr=[]
testCase=int(input())
for _ in range(testCase):
    No_len=int(input())
    No=input()
    outputStr.append(convert_palindrome(No_len,No))

for i in range(testCase):
    print(f"Case #{i+1}: {outputStr[i]}")