a=int(input("Enter any number="))
b=int(input("Enter any number="))
c=int(input("Enter any number="))
d=int(input("Enter any number="))
if(a>b and a>c and a>d):
    print(a,"is greater")
elif(b>a and b>c and b>d):
    print(b,"is greater")
elif(c>a and c>b and c>d):
    print(c,"is greater")
elif(d>a and d>b and d>c):
    print(d,"is greater")
else:
    print("All maybe equal")    
