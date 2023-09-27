with open("prb09f_log_file.txt") as f:
    content1=f.read()
with open("prb09h_this.txt") as f:
    content2=f.read()
if content1==content2:
    print("Both files are identical")
else:
    print("they are not identical")
