# class Self_demo:
#     def method_a(self):
#         print("now in method a")
#         print("i am method a")
#     def method_b(self):
#         print("in method b calling method a")
#         self.method_a()  #calling method a
# a=Self_demo()
# a.method_b()


# class fg:
#     def grt(self,a,b):
#         z=a
#         print("Greater number is: ",a)
#     else:


# ACCESSIBILITY
# To make an attribute and a method private we need to add two things
# class Person:
#     def __init__(self):
#         self.name='ishan' #public attribute
#         self.__bankaccno=10101 #private attribute
#     def Display(self):
#         print("name is: ",self.name)
#         print("bank account number is: ",self.__bankaccno)
# P=Person()
#print(P.name)
# P.Display()
#print(P.__bankaccno)
#print(P._Person__bankaccno)
#P.Display


#attributes and __init__method
#we can initialize the value of a member variable or attribute
class Circle:
    pi=0
    radius=0
    def __init__(self):
        self.pi=3.14
        self.radius=5
    def calc_area(self):
        print(self.radius)
        return self.pi*self.radius**2
c1=Circle()
print(c1.calc_area())


class box:
    width=0
    height=0
    depth=0
    vol=0
    def __init__(self):
        self.width=5
        self.height=5
        self.depth=5
        print(self.width*self.height*self.depth)
    def vol(self):
        print('width= ',self.width)
        print('height= ',self.height)
        print('depth= ',self.depth)
        return self.width*self.height*self.depth
b1=box()
print('volume of cube is = ',b1.vol())
