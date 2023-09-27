# use open function to open a file
# f=open("09a_sampleFile.txt") #by defualt read only is present
f=open("09a_sampleFile.txt","r") 
write=f.read() #would read all of it
# write=f.read(5) #would read only five characters
print(write)
f.close()
print(type(f))