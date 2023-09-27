# problem 09f
""" with open("prb09f_log_file.txt") as f:
    book=f.read()
if "python" in book.lower():
    print("Yes Python is present")
else:    
    print("No Python is  not present")"""

# problem 09g also print line number
book=True
statement=True
i=1
with open("prb09f_log_file.txt") as f:
    while(book):
        book=f.readline()
        if "python" in book.lower():
            print("Python is present at line#"+str(i))
            statement=False
        i=i+1
if statement:
    print("no python is not present")