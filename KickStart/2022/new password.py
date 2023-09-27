def passwordChange(no):
    string=input()
    specialChar=['#','@','*','&']
    special=True
    uc=True
    lc=True
    digit=True

    for i in string:
        if i in specialChar and special==True:
            special=False
        if i.isdigit and digit==True:
            digit=False
        if i.isupper() and uc==True:
            uc=False
        if i.islower() and lc==True:
            lc=False

    if(special):
        string=string+'#'
    if(digit):
        string=string+'0'
    if(uc):
        string=string+'A'
    if(lc):
        string=string+'a'

    filler = "aB4*Hba"
    if (len(string) < 7):
        string += filler[0:7-len(string)]
    
    return string

outputStr=[]
testCase=int(input())

for _ in range(testCase):
    no=int(input())
    outputStr.append(passwordChange(no))

for i in range(testCase):
    print(f"Case #{i+1}: {outputStr[i]}")