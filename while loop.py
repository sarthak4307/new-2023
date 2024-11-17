a=int(input())
c=0
n=2
while(n<=a):
    if(a%n==0):
        c=c+1
    n=n+1
if(c>=2):
    print("not prime")
if(c<=1):
    print("prime")
