def greatest(a,b,c):
    if(a>b and a>c):
        print(a," is greatest number")
    elif b>c and b>a:
        print(b," is greatest number")
    elif c>a and c>b:
        print(c," is greatest number")
    else:
        print("At least two greater number will be equal")
p=int(input("Enter a number="))        
q=int(input("Enter a number="))        
r=int(input("Enter a number="))
greatest(p,q,r)        