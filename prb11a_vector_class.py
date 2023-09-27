import math
class Vector2D:
    def __init__(self):
        self.x=int(input("Enter x-axis length="))
        self.y=int(input("Enter y-axis length="))
    def __add__(self,Vector):
        return math.sqrt((self.x-Vector.x)**2+(self.y-Vector.y)**2)
class Vector3D(Vector2D):
    def __init__(self):
        super().__init__()
        self.z=int(input("Enter z-axis length="))
    def __add__(self, Vector):
        return math.sqrt((self.x-Vector.x)**2+(self.y-Vector.y)**2+(self.z-Vector.z)**2)
    # problem 11f representing 3d vector as xi+yj+zk
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
v1=Vector2D()
v2=Vector2D()
print("Sum=",v1+v2)
v11=Vector3D()
v22=Vector3D()
print("Sum=",v11+v22)
# problem 11f representing 3d vector as xi+yj+zk
print(v11)