class Complex:
    def __init__(self,r,i):
        self.a=r
        self.b=i
    def __add__(self,c1):
        return Complex((self.a+c1.a),(self.b+c1.b))
        
    def __mul__(self,c1):
        a=(self.a*c1.a)-(self.b*c1.b)
        b=(self.a*c1.b)+(self.b*c1.a)
        return Complex(a,b)
    def __str__(self):
        return f"{self.a} + {self.b}i"
c1=Complex(3,4)
c2=Complex(2,5)
print(c1+c2)
print(c1*c2)