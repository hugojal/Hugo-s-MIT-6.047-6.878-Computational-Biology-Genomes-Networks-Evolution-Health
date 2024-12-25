# Manhattan's Tourist problem implementation, 4x4 grid

import numpy as np

# Generate random weights for the edges
w1 = np.random.randint(8, size=(4,4))
w2 = np.random.randint(8, size=(4,4))

# Grid dim
n, m = 4, 4

# Init grid
M = [[0 for _ in range(n+1)] for _ in range(m+1)]
M[0][0] = 0

# Fill grid
for i in range(n):
  M[i+1][0] = w1[0][i]

for j in range(m):
  M[0][j+1] = w2[0][j]

for i in range(1, n+1):
  for j in range(1, m+1):
    east = M[i][j-1] + w2[i-1][j-1]
    south = M[i-1][j] + w1[i-1][j-1]

    M[i][j] = max(east, south)

# Traceback mechanic
path = []

i, j = n, m

while i > 0 or j > 0:
    path.append((i, j))
    
    if i > 0 and j > 0:
        decision = max(int(M[i][j-1]), int(M[i-1][j-1]), int(M[i-1][j]))
        
        if decision == int(M[i][j-1]):
            j -= 1 
        elif decision == int(M[i-1][j-1]):
            i -= 1  
            j -= 1
        else:
            i -= 1  
    elif i > 0: 
        i -= 1
    else:  
        j -= 1

path.append((0, 0))  
path.reverse()  

print(path)
