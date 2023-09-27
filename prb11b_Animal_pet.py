class Animal:
    def __init__(self):
        self.name=input("Enter name:")
    def eat(self):
        print("Animal is eating")
    def sleep(self):
        print("Animal is sleeping")

class Pet(Animal):
    def __init__(self):
        super().__init__()
    def eat(self):
        print("Pet is eating")
    def sleep(self):
        print("Pet is sleeping")

class Dog(Pet):
    def eat(self):
        print("Dog is eating")
    def sleep(self):
        print("Dog is sleeping")
    def Bark(self):
        print("wowooww")
doggy=Dog()
doggy.Bark()