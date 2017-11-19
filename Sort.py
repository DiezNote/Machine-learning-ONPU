import numpy as np
import matplotlib.pyplot as plt
import random

def sort(massiv):
 for j in range(len(massiv)):
    for i in range(len(massiv)-j-1):
        if massiv[i] > massiv[i+1]:
            f=massiv[i]
            massiv[i]=massiv[i+1]
            massiv[i+1]=f
 return massiv

X = np.random.randint(-20,20,30)
Y = np.random.randint(-20,20,30)
fig=plt.figure()
plt.plot(X,Y,'green')
print(X)
print(Y)

F=sort(X)
H=sort(Y)

plt.plot(X,Y,'green',F,H,'red')

plt.show()

print(F)
print(H)
