def Sum(n):
    if n==0:
        return 0
    else:
        return n+Sum(n-1)
a=int(input("Enter a number="))
print(Sum(a))