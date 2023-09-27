class NDimVector:

    def __init__(self,dim):
        self.dim=dim

    def __len__(self):
        return len(self.dim)

    def __str__(self):
        str1=""
        for i in range(0,len(self)):
            str1=str1+f"{self.dim[i]}a{i} + "
        return str1[:-2]

    def __add__(self,v1):
        if len(self)==len(v1):
            for i in range(0,len(self)):
                self.dim[i]=self.dim[i]+v1.dim[i]
            return self
        else:
            print("not possible")
            return None

    def __mul__(self,v1):
        multiple=0
        if len(self)<len(v1):
            less=len(self)
        else:
            less=len(v1)
        for i in range(0,less):
            multiple+=self.dim[i]*v1.dim[i]
        return multiple
        
v1=NDimVector([1,2,3])
v2=NDimVector([1,2,3])
print(v1+v2)
print(v1*v2)
print(len(v1))