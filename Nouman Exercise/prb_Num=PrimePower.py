num=8
def primeNo(num):
    for i in range(2,int(num/2)+1):
        if num%i==0:
            return False
    else: return True
def power(divider):
    global num
    i=0
    while(num):
        if num%divider==0:
            i+=1
            num=num/divider
        else:
            break
    return i
for i in range(2,num):
    if not(primeNo(i)):
        continue
    elif num%i==0:
        print(i,end=" ")
        print(power(i),end=" ")
if num!=1:
    print(num)