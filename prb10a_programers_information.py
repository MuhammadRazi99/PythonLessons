class Programer:
    company="Microsoft"
    workingHours=8
    salery=10000
    def __init__(self,a,b):
        self.setPersonalInfo(a,b)
        
    def setPersonalInfo(self,a,b):
        self.EmployeeName=a
        self.EmployeeNo=b

    def DisplayInfo(self):
        print("Name="+self.EmployeeName)    
        print("Company="+self.company)
        print("Employee no=",self.EmployeeNo)    
        print("Salery=",self.salery)
        print("Working Hours=",self.workingHours)

Razi=Programer("Razi",10001)
Razi.DisplayInfo()

    