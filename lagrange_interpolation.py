import numpy as np
x = [0.8, 1.0, 0.7, 0.6]
y = [0.22363362, 0.65809197, 0.01375227, -0.17694460]
n = len(x)
X = 0.9
S = 0
L = np.zeros((n,1))
for i in range(n):
    L[i] = 1
    for j in range(n):
        if j!=i:
            L[i] = (X - x[j])/(x[i]-x[j])
    S += L[i] * y[i]
print(S)    
    