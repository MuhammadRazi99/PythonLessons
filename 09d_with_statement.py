with open('09c_sampleFile.txt', 'r') as f:
    a = f.read()
with open('09c_sampleFile.txt', 'w') as f: #does not need to close the file
    a = f.write("me")
print(a)
