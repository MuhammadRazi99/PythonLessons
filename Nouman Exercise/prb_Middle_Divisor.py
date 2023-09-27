def primeNo(num):
    for i in range(2,int(num/2)+1):
        if num%i==0:
            return False
    else: return True
with open("in1.txt") as f:
    loop=int(f.readline())
    for i in range(0,loop):
        num=int(f.readline())
        divisiors=[]
        if primeNo(num):
            print(1)
        else:
            for i in range(2,num):
                if num%i==0:
                    divisiors.append(i)
            if len(divisiors)%2==0:
                a=int(len(divisiors)/2)-1
                print(divisiors[a])
            else:
                a=int(len(divisiors)/2)
                print(divisiors[a])
