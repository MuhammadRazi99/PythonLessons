def Table(no):
    for i in range(1,11):
        print(str(no)+"x"+str(i)+"="+str(i*no))
a=int(input("Enter a number:"))
Table(a)