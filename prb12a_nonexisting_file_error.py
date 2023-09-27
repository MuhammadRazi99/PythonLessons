""" try:
    f=open("1.txt")
    f.close()
except Exception as e:
    print("1.txt is not present here!")

try:
    f=open("2.txt")
    f.close()
except Exception as e:
    print("2.txt is not present here!")

try:
    f=open("3.txt")
    f.close()
except Exception as e:
    print("3.txt is not present here!")

print("Thanks for using this program")
 """
# alternative method which is much better
def readFile(filename):
    try:
        f=open(filename,"r")
        f.close()
    except Exception as e:
        print(filename+" is not found")

readFile("1.txt")
readFile("2.txt")
readFile("3.txt")
print("Thanks for using this program")