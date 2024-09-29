import numpy as np
x = [8.3, 8.6, 8.7, 8.1]
y = [17.56492, 18.50515, 18.82091, 16.94410]
n = len(x)
X = 8.4
S = 0
L = np.zeros((n,1))
for i in range(n):
    L[i] = 1
    for j in range(n):
        if j!=i:
            L[i] *= (X - x[j])/(x[i]-x[j])
    S += L[i] * y[i]
print(S)    
    