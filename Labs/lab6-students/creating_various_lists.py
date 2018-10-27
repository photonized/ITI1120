import random

n=int(input("Enter a positive even integer for the size of the list?" ))
i=0
a=[]
b=[]
c=[]
d=[]
e=[]

#p1.1
while i<n:
    a+=[0]
    i+=1
print(a)

#p1.2
a=[0]*n

print(a)


#p2.1
for i in range(n):
    r=random.randint(1,100)
    b+=[r]
print(b)

#p2.2
b=[random.randint(1, 100) for i in range(n)]
print(b)

#p3.1
c=[]
c=b
print(id(b), b, id(c), c)

#p3.2
c=[]
c=b
c*=2
print(id(c), c, id(b), b)

#p4.1
c=[0]*(n//2)+b[n//2:n]
print(b, c)

#p4.2
c=[]
for i in range(n//2):
    c+=[0]
for i in range(n//2, n):
    c+=[b[i]]
print(b,c)

#p5.1
d=[]
for i in range(len(b)):
    d+=[b[i]]
print(d, id(d))

#p5.2
d=[]
d+=b
print(d, id(d))

#p6.1
for i in range(n):
    if i%2 != 0:
        e+=[b[i]]
print(e)

#p6.2
e=[]
while i < n:
    if not i%2==0:
        e+=[b[i]]
    i+=1
print(e)