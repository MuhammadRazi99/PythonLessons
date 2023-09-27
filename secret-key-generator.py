import sys
def getDataKey(inputString):
    l1=inputString.split(",")
    strReturn=""
    for value in l1:
        if len(value)!= 1:
            strReturn+=getsum(value)
            strReturn+=" "
        else:
            strReturn+=value
            strReturn+=" "
    return strReturn
def getsum(strNO):
    if len(strNO)==1:
        return strNO
    else:
        lno1=list(strNO)
        lno2=[]
        for value in lno1:
            if value!=" ":
                lno2.append(int(value))
        intNo=sum(lno2)
        strT=getsum(str(intNo))
        return strT

fh = open(sys.argv[1],'r')
fn = open('output-ch3.txt','w')
fn.write('')
for line in fh:
	newString = getDataKey(line)
	with open('output-ch3.txt', "a") as myfile:
		myfile.write(newString)