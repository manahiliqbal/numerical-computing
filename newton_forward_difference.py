import numpy as np
import math

x = [0, 0.25, 0.5, 0.75]
y = [1, 1.64872, 2.71828, 4.48169]
n = len(x)
X = 0.43
h = x[1] - x[0]
F = np.zeros((n,n))

for i in range(n):
    F[i,0] = y[i]
    
for i in range(1,n):
    for j in range(1, i+1):
        F[i,j] = F[i,j-1] - F[i-1,j-1] 
        
P = (X - x[0])/h      
m = np.zeros((n,1))
m[0] = 1
S = F[0,0] 

for i in range(1,n):
    m[i] = m[i-1]*(P-i+1)  
    S += m[i]*(F[i,i]/math.factorial(i)) 
    
print(S)    
     