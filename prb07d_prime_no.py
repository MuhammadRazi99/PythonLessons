no=int(input("Enter a number:"))
for i in range(2,int(no/2)+1):
    if(no%i==0):
        print(no,"is not a prime no")
        exit()
print(no,"is a prime no")  