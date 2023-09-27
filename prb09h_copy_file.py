with open("prb09f_log_file.txt") as f:
    content=f.read()
with open("prb09h_this.txt","w") as f:
    f.write(content)