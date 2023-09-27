def passwordChange(no):
    string = input()
    specialChar = ['#', '@', '*', '&']

    special = True
    uc = True
    lc = True
    digit = True

    for i in string:
        if i in specialChar:
            special = False

        if i >= '0' and i <= '9':
            digit = False

        if i >= 'A' and i <= 'Z':
            uc = False

        if i >= 'a' and i <= 'z':
            lc = False

    newString = string
    if(special):
        newString += '@'
    if(digit):
        newString += '3'
    if(uc):
        newString += 'A'
    if(lc):
        newString += 'd'

    filler = "aB4*Hba"
    if (len(newString) < 7):
        newString += filler[0:7-len(newString)]

    return newString


t = int(input())
for i in range(1, t + 1):

    n = int(input())
    print("Case #{}: {}".format(i, passwordChange(n)))
