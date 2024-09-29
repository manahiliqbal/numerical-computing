import numpy as np

x = [8.1, 8.3, 8.6, 8.7]
y = [16.94410, 17.56492, 18.50515, 18.82091]

n = len(x)
X = 8.4
D = np.zeros((n,n))

for i in range(n):
    D[i,0] = y[i]
    
S = D[0,0] 
m = np.zeros((n,1))
m[0] = 1
   
for i in range(1,n):
    for j in range(1, i+1):
        D[i,j] = (D[i, j-1] - D[i-1, j-1]) / (x[i] - x[i-j]) 
print(D)

for i in range(1,n):
    m[i] = m[i-1] * (X - x[i-1])
    S += m[i] * D[i, i]
    
print(S)