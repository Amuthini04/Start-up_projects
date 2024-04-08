import numpy as np
def f(x):
    return x*(10-x)/100
def g(x):
    return 0

iteration = eval(input("enter the number of iterations:"))
row = eval(input("enter the number of boundary values:"))
u = [[0.0 for c in range(iteration+1)] for r in range(row)]
for i in range(row):
    u[i][0] = f(i*2)

c = eval(input("enter the value of c:"))
h = eval(input("enter the value of h:"))
k = eval(input("enter the value of k:"))
r = (c**2)*(k**2) / (h**2)
print("the value of r",r)
j = 0

for i in range(1,row-1):
    u[i][j+1] = (r*(u[i+1][j]+u[i-1][j])/2)+(1-r)*u[i][j]+2*k*g(i*2)

print("the starting condition is")
for i in range(row):
    for j in range(iteration):
        print(round(u[i][j],2),end="\t")
    print("\n")
for j in range(1,iteration):
    for i in range(1,row-1):
        u[i][j+1] = r*(u[i-1][j]+u[i+1][j])+2*(1-r)*u[i][j]-u[i][j-1]

print("the solution for the equation is")
for i in range(row):
    for j in range(iteration):
        print(round(u[i][j],2),end="\t")
    print("\n")