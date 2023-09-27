def remove_strip(string,word):
    newStr=string.replace(word," ")
    return newStr.strip()
a=input("Enter a string:")
b=input("Enter a string word:")
print(remove_strip(a,b))