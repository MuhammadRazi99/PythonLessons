""" def func1(a):
    if a%5==0: 
        return True
    else:
        return False """
# func1 and func2 are equal
func2=lambda a:a%5==0
l=[1,3,5,10,23,15,23,45,67,70]
print(list(filter(func2,l)))