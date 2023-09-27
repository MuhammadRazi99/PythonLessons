no=int(input("Enter a number:"))
l=[i*no for i in range(1,11)]
print(l)
with open("prb12c_table.txt","w") as f:
    for item in l:
        f.write(str(item)+"\n")