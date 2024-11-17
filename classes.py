# class test:
#     a=0
#     b=0
#     def __init__(self,x,y):
#         self.a=x
#         self.b=y
#     def equal(self,abc):
#         if(abc.a==self.a and abc.b==self.b):
#             return True
#         else:
#             return False
# obj1=test(10,20)
# obj2=test(10,20)
# obj3=test(12,90)
# print(obj1.equal(obj2))
# print(obj1.equal(obj3))


# class rect:
#     len=0
#     wid=0
#     def __init__(self,l,w):
#         self.len=l
#         self.wid=w
#     def area(self,obj):
#         print(obj.len)
#         print(obj.wid)
#         return obj.len*obj.wid
# obj1=rect(10,20)
# print(obj1.area(obj1))  


# class sphere:
#     radius=0
#     def __init__(self,r):
#         self.radius=r
#     def volume(self,obj):
#         print(obj.radius)
#         return (4/3)*3.14*obj.radius**3
# obj1=sphere(4)
# print(obj1.volume(obj1))


# class demo:
#     def __init__(self):
#         print('welcome')
#         def __del__(self):
#             print('dectructor executed successfully')
# ob1=demo()
# ob2=ob1
# ob3=ob1
# print("id of ob1= ",id(ob1))
# print("id of ob3= ",id(ob2))
# print('id of ob3= ',id(ob3))
# del ob2
# del ob1
# # del ob3
# # print(id(ob1))            #gives error because we deleted all the objects
# # print(id(ob2))
# print(id(ob3))

# #we now make more objects 
# ob1=demo()
# ob2=ob1
# print('updated id of ob1= ',id(ob1))
# print('updated id of ob2= ',id(ob2))
# print("old id of ob3",id(ob3))
# ob3=ob1
# print("updated id of ob3",id(ob3))


# method overriding in Python
class overload:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
# python will over-ride the first function over second
o1=overload()
# o1.add(100,20)         # if we run this it shows error because only a and b is dfined not c
o1.add(100,20,10)


# operator over-riding
