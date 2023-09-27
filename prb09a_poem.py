f=open("prb09a_poem.txt")
poem=f.read()
f.close()
if poem.find("twinkle")!=-1:
    print("Yes, their is Twinkle present in the poem")
else:
    print("No, their is not Twinkle present in the poem")