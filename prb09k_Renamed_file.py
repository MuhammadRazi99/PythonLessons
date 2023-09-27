import os
oldName="prb09k_oldFile.txt"
NewName="prb09k_Renamed_by_Python.txt"
oldFile=open(oldName)
old=oldFile.read()
oldFile.close()
newFile=open(NewName,"w")
newFile.write(old)
newFile.close()
os.remove(oldName)