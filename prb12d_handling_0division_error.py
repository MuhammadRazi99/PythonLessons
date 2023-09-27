def division(a,b):
    try:
        int(a)/int(b)
    except ZeroDivisionError as e:
        return "Infinity"
    except Exception as e:
        return "wrong input"
    else:
        return int(a)/int(b)
num1=input("Enter a number:")
num2=input("Enter a number:")
print(division(num1,num2))