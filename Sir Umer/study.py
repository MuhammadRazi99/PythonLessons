from dataclasses import replace
func =lambda n:int(n,2)
def countDown(num,max):
    while(num<=max):
        print(num)
        print()
        print()
        print()
        num+=1
def Binary8(string):
    binaryString='00000000'
    string=string[2:]
    if len(string)<8:
        string=binaryString[0:8-len(string)]+string
        return string
    else:
        return string 
def Binary4(string):
    binaryString='0000'
    string=string[2:]
    if len(string)<4:
        string=binaryString[0:4-len(string)]+string
        return string
    else:
        return string   
def ConvertIntoBin(Dstr):
    l1=[]
    l1=map(int,Dstr.split('.'))
    l1=map(bin,l1)
    l1=map(str,l1)
    l1=map(Binary8,l1)
    string='.'.join(l1)
    return string
def ConvertIntoDec(Bstr):
    l1=[]
    l1=map(func,Bstr.split('.'))
    l1=map(str,l1)
    string='.'.join(l1)
    return string

def BinaryLoop(num,max):
    while(num<=max):
        print(ConvertIntoBin(str1.replace(' ',str(num))))
        print(ConvertIntoBin(str2.replace(' ',str(num))))
        num+=1
        print(ConvertIntoBin(str3.replace(' ',str(num))))
        print(ConvertIntoBin(str4.replace(' ',str(num))))
        num+=1
def DecimalLoop(num,max):
    while(num<=max):
        print(str1.replace(' ',str(num)))
        print(str2.replace(' ',str(num)))
        num+=1
        print(str3.replace(' ',str(num)))
        print(str4.replace(' ',str(num)))
        num+=1

str1='192.168. .0'
str2='192.168. .1'
str3='192.168. .254'
str4='192.168. .255'
DecimalLoop(0,255)


# str1='10101100.0001----.00000000.00000000'
# str2='10101100.0001----.00000000.00000001'
# str3='10101100.0001----.01111111.11111110'
# str4='10101100.0001----.01111111.11111111'
# str5='10101100.0001----.10000000.00000000'
# str6='10101100.0001----.10000000.00000001'
# str7='10101100.0001----.11111111.11111110'
# str8='10101100.0001----.11111111.11111111'
# def BinaryLoop(num,max):
#     while(num<=max):
#         a=bin(num)
#         a=Binary4(a)
#         print(ConvertIntoDec(str1.replace('----',a)))
#         print(ConvertIntoDec(str2.replace('----',a)))
#         print(ConvertIntoDec(str3.replace('----',a)))
#         print(ConvertIntoDec(str4.replace('----',a)))
#         print(ConvertIntoDec(str5.replace('----',a)))
#         print(ConvertIntoDec(str6.replace('----',a)))
#         print(ConvertIntoDec(str7.replace('----',a)))
#         print(ConvertIntoDec(str8.replace('----',a)))
        
#         # print(str1.replace('----',a))
#         # print(str2.replace('----',a))
#         # print(str3.replace('----',a))
#         # print(str4.replace('----',a))
#         # print(str5.replace('----',a))
#         # print(str6.replace('----',a))
#         # print(str7.replace('----',a))
#         # print(str8.replace('----',a))
#         num+=1
# BinaryLoop(0,15)