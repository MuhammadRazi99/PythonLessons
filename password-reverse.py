def getnewPassword(inputString):
    l2=""
    l3=""
    for value in inputString: 
        if (ord(value)>=65 and ord(value)<=90) or (ord(value)>=97 and ord(value)<=122):
            l2+=value
    print(l2)
    i=len(l2)-1
    for value in inputString: 
        if (ord(value)>=65 and ord(value)<=90) or (ord(value)>=97 and ord(value)<=122):
            l3+=l2[i]
            i-=1
        else:
            l3+=value
    return l3
with open("input-ch1.txt") as f:
    inputstr=f.read()
with open("output-ch1.txt","w") as f:
    f.write(getnewPassword(inputstr))       