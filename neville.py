import numpy as np
import math
x = [8.1, 8.3, 8.6, 8.7]
n = len(x)
y = [16.94410, 17.56492, 18.50515, 18.82091]
X = 8.4

Q = np.zeros((n, n))
for i in range(n):
    Q[i,0] = y[i]
    
for i in range(1, n):
    for j in range(1, i+1):
        Q[i,j] = (Q[i,j-1]*(X-x[i-j]) - Q[i-1, j-1]*(X-x[i]))/ (x[i]-x[i-j])

print(Q)        