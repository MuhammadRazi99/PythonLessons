class Sample:
    a=10
obj=Sample()
obj.a=0
print("Object a=",obj.a)
print("Sample a=",Sample.a)
# if we change using obj.a then it will change the instance variable
# when we will change using Sample.a then it will change the class variable