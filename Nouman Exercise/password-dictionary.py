def getBruteforceDictionary(inputString):
    inputString=inputString[1:-1]
    inputString=inputString.replace("'","")
    l1=inputString.split(",")
    sameValue=True
    l2=[]
    for values in l1:#cat,act
        set1={values} #cat
        for items in l1: #tac
            if len(values)==len(items): #true
                for i in values:#
                    if items.find(i)==-1:
                        sameValue=False
                        break 
                if(sameValue):
                    set1.add(items)
        l2.append(set1)
        del set1 
    print(l2)


getBruteforceDictionary("['cat','dog','tac','act']")
    # input-> ['cat','dog','God']
    # output->[{'cat'},{'dog','God'}]