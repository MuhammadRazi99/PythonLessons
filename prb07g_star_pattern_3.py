n=3
for i in range(n):
    if i==0 or i==n-1:
        print("x"*n)
    else:
        print("x"+" "*(n-2)+"x")