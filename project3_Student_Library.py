from typing import List
class Student:
    def studentInfo(self):
        self.name=input("Enter your name:")
        self.rollno=input("Enter your Rollno:")
        self.classSection=input("Enter your class and section=")
        self.phoneNo=input("Enter your phone no:")
        self.address=input("Enter your address:")
        self.password=input("Enter a strong password:")
        self.l=[self.name,self.password,self.rollno,self.classSection,self.phoneNo,self.address]
        return self.l
    def getStudentDetails(self,name):
        with open("project3_Student.txt") as f:
            content=True
            while(content):
                content=f.readline()
                self.l=List(content)
                print(self.l)   #noted
                if name==self.l[0]:
                    break
            if content==False:
                print("we can find your name try again")
                pass
        self.name=self.l[0]
        self.password=self.l[1]
        self.rollno=self.l[2]
        self.classSection=self.l[3]
        self.phoneNo=self.l[4]
        self.address=self.l[5]
    def __str__(self):
        return f'''Name:{self.name}\nPassword:{self.password}\nRoll no:{self.rollno}\n
        Class and Section:{self.classSection}\nPhone No:{self.phoneNo}\nAddress:{self.address}'''

class Library:
    pass

class StudentLibrary(Student,Library):
    pass

condition=True
while(condition):
    print("...Student Login...")
    account=input("1.Login\n2.SignUp\n3.To exit type 'exit()'\n>>>")
    if account=="exit()":
        break
    elif account.lower()=="login":
        newStudent=Student()
        l=newStudent.studentInfo()
        with open("project3_Student.txt","a") as f:
            f.write(str(l)+"\n")

    elif account.lower()=="signup":
        student1=Student()
        username=input("Enter your name:")
        student1.getStudentDetails(username)
        print(student1)

    else:
        print("wrong input please write in lower case:")
    # print("To exit this program please write 'exit()'\n>>>")
    print("Thanks for using online Library")