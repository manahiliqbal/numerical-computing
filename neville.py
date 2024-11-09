import numpy as np

x = [8.1, 8.3, 8.6, 8.7]
y = [16.94410, 17.56492, 18.50515, 18.82091]
n = len(x)

Q = np.zeros((n, n))
Q[:, 0] = y

c = float(input('Enter x: '))
for i in range(1, n):
    for j in range(1, i + 1):
        Q[i, j] = ((c - x[i - j]) * Q[i, j - 1] - (c - x[i]) * Q[i - 1, j - 1]) / (x[i] - x[i - j])

print('Q=')
print(Q)       