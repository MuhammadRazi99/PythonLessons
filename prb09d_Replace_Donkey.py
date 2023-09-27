with open("prb09d_donkey.txt") as f:
    content=f.read()
content=content.replace("donkeys","######")    
with open("prb09d_donkey.txt","w") as f:
    f.write(content)    

# prb09e cencerded words
""" l=["monkey","donkey","f word"]
with open("prb09d_donkey.txt") as f:
    content=f.read()
for value in l:
    content=content.replace(value,"######")    
with open("prb09d_donkey.txt","w") as f:
    f.write(content)     """