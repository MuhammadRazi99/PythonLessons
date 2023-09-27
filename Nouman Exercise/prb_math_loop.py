no=int(input("Enter a number="))
loop=[]
loop.append(no)
while(no!=1):
    if no%2==0:
        no=2
        loop.append(no)
    else:
        no=3*no+1
        loop.append(no)
print(len(loop))
