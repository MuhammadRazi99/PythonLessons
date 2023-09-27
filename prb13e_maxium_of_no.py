from functools import reduce
def func(a,b):
    if a>b: 
        return a
    else:
        return b
# build in function max and min are present
l1=[1,3,5,10,23,15,23,45,67,70]
l2=reduce(max,l1)
print(l2) 