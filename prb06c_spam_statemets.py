statements=input("Enter any statement:")
if(statements.find("make a lot of money")!=-1):
    print("spam")
elif(statements.find("buy now")!=-1):
    print("spam")
elif(statements.find("subscribe this")!=-1):
    print("spam")
elif(statements.find("click this")!=-1):
    print("spam")
else:
    print("not a spam")        

# other way:
""" text = input("Enter the text\n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")  """