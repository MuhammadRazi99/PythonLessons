for i in range(2,21):
    f=open(f"13 Years Old\\Multiplication_Table_of_{i}.txt","w")
    for j in range(1,11):
        f.write(str(i)+"x"+str(j)+"="+str(i*j))
        if(j!=10):
            f.write("\n")
    f.close()