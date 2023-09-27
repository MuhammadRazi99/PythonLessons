import random
class PakistaniTrain:
    def bookTicket(self):
        self.Name=input("Enter your name:")
        self.CNIC=int(input("Enter your CNIC no without dashes="))
        self.trainName=input("choose the train name from the following:\n1.Islamabad Express\n2.Green Line\n3.Fareed Express\n>>")
        self.className=input("Choose the class name:\n1.Bussiness\n2.Parlour\n3.Economy\n>>")
        self.noOfSeat=int(input("Enter the no of seat you want to book="))
    def getStatus(self):
        firstSeat=random.randint(1,50)
        print("no of your seats=",end="")
        for i in range(firstSeat,firstSeat+self.noOfSeat):
            print(str(i)+",",end="")
        print()
    def fare(self):
        if self.className=="Bussiness":
            print("Fare=",600*self.noOfSeat)
        elif self.className=="Parlour":
            print("Fare=",800*self.noOfSeat)
        elif self.className=="Economy":
            print("Fare=",400*self.noOfSeat)
        else:
            print("you selected the unavaiable class")
train=PakistaniTrain()
train.bookTicket()
train.getStatus()
train.fare()