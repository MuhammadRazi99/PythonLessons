l=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
def powr(primeNo):
    i=1
    global num
    while pow(primeNo,i)<num:
        i+=1    
    num=num-pow(primeNo,i-1)
    return i-1
with open("in3.txt") as f:
    loop=int(f.readline())
    for i in range(0,loop):
        num=int(f.readline())
        for item in l:
            print(item,end=" ")
            print(powr(item),end=" ")
            if item>num:
                print(num)
                break
        