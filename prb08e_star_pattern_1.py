def pattern(n):
    if n==0:
        return ""
    else:
        print("x"*n)
        pattern(n-1)
a=int(input("Enter a number="))
pattern(a)