# problem 05f: assuming name are unique
""" myDic={}
myDic.update({"Ahmed":"English","Nabeel":"Urdu","Ammar":"Arabic","Hamza":"Greek"})
print(myDic)"""

# problem 05g: name are not unique
""" myDic={}
myDic.update({"Ahmed":"English","Nabeel":"Urdu","Ammar":"Arabic","Ahmed":"Greek"})
print(myDic)"""
# it will update even if it is not written at the update menu but in the MyDic orginal syntax

# problem 05h: values are not unique
myDic={}
myDic.update({"Ahmed":"English","Nabeel":"Urdu","Ammar":"Arabic","Hamza":"English"})
print(myDic)
# nothings happens nor matters