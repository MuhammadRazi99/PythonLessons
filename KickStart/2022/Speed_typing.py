def check_typing(correct,incorrect):
    count=0
    for i in range(len(incorrect)): 
            if (len(correct)>len(incorrect)):
                return "IMPOSSIBLE"
            if(correct[i]==None):
                incorrect=incorrect[:i]+incorrect[i+1:]
                count+=1
            elif(not(incorrect[i] == correct[i])):
                incorrect=incorrect[:i]+incorrect[i+1:]
                count+=1
            
    if(incorrect==correct):
        return count
    else:
        return "IMPOSSIBLE"

outputStr=[]
testCase=int(input())
for _ in range(testCase):
    I=input()
    P=input()
    outputStr.append(check_typing(I,P))
print("present")
print(outputStr)
for i in range(testCase):
    print(f"Case #{i+1}: {outputStr[i]}")