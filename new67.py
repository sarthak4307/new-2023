l1=[2,6,8]
l2=['x','y','z']
l3=[9,7,6]

l1.extend(l2)
print(l1)

print(l1.index(2))

l1.insert(2,50)
print(l1)

l1.reverse()
print(l1)

l3.sort()
print(l3)

import random
print(random.random())
print(random.randint(0,6))  # range = (0,6]


# Aliasing
a=[1,2,3]
b=a              # we are passing adress of "a" to "b"
b[0]=5
print(a)
print(id(a),id(b))

# Cloning
a=[1,2,3]
b=a.copy()          # we are passing the elements of "a" to "b"
b[0]=5
print(a)
print(b)
print(id(a),id(b))

a=[1,2,3]
b=a[:]              # we are passing the elements of "a" to "b"
b[0]=5
print(a)
print(b)
print(id(a),id(b))


