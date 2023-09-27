math=int(input("Enter the marks of Math="))
phy=int(input("Enter the marks of Physics="))
chem=int(input("Enter the marks of Chemistry="))
# assuming total marks were from 100
if(math>=33 and phy>=33 and chem>=33):
    if(math+phy+chem)/3>=40:
        print("pass")
    else: print("fail")
else: print("fail")