t=float(input())
s=0
g=0
n=0
while t!=0:
    s=s+t
    g=g+t**2
    t=float(input())
    n+=1
m=(g/(n-1)-((s/n)**2)*n/(n-1))**0.5
b=m/(n**0.5)
print(b)
print(s/n)
input()
