a = 8

# 1. if-elif-else ladder in Python
""" if(a<3): 
    print("The value of a is greater than 3")
elif(a>13):
    print("The value of a is greater than 13")
elif(a>7):
    print("The value of a is greater than 7")
elif(a>17):
    print("The value of a is greater than 17")
else:
    print("The value is not greater than 3 or 7")"""

# 2. Multiple if statements
if(a<3): 
    print("The value of a is greater than 3")

if(a>13):
    print("The value of a is greater than 13")
    
if(a>7):
    print("The value of a is greater than 7")

if(a>17):
    print("The value of a is greater than 17")
else:
    print("The value is not greater than 3 or 7")

print("Done")

# is else optional
a = 6
if(a==7):
    print("yes")
elif(a>56):
    print("no and yes")
else:
    print("I am optional")
