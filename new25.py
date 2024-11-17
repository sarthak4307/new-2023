l=list(range(0,6))
print(l)            # prints [0,1,2,3,4,5]


n=900
i=0
while(i<=n):
    print(i)
    i+=100


A=["a","b"]
B=["a","b"]
print(id(A))
print(id(B))
print(A is B," adress of A and B is diffrent")
A=B
print(id(A))
print(id(B))
print(A is B)


m=[1,2,3,4,5]
del(m[2])
print(m)


# list comprehension method
l1=[10,20,30,40,50,60,70,78,90]
l1=[x+10 for x in l1]
print(l1)
l1=[x for x in l1 if x%11==0]
print(l1)


l1=['x','y','z']
l2=l1.copy()
print(l2)
print("Adress of l1=",id(l1),";","ID of l2",id(l2),sep="  ")


a=["1","2","3","4","5"]
for i in a:
    print(i,end=" ")




