class Employee:
    salery=10000
    increment=2.5
    @property
    def saleryAfterIncrement(self):
        return self.salery+(self.increment*100)/self.salery
    @saleryAfterIncrement.setter
    def saleryAfterIncrement(self,val):
        self.increment=(val-self.salery)*self.salery/100
e=Employee()
print("Salery=",e.saleryAfterIncrement)
e.saleryAfterIncrement=15000
print("previous salery=",e.salery)
print("Increment=",e.increment)        
