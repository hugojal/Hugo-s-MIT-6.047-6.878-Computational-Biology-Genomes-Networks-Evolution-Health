# This is the implementation of the Needleman-Wunch algorithm after listening to the lecture by Manolis Kellis. Different penalties are applied for mutation types.

import random
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

def nw(seq1, seq2, match_score=1, transition_penalty=-1, transversion_penalty=-2, gap_penalty=-0.5):
    purines = ['A', 'G']
    pyramidines = ['C', 'T']

    # Initialize matrix
    m, n = len(seq1), len(seq2)
    M = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Initialize the first row and column with gap penalties
    for i in range(m + 1):
        M[i][0] = gap_penalty * i
    for j in range(n + 1):
        M[0][j] = gap_penalty * j

    def get_score(a, b):
      if a==b:
        return match_score
      elif (a in purines and b in purines) or (a in pyramidines and b in pyramidines):
        return transition_penalty
      else:
        return transversion_penalty

    # Fill the scoring matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = M[i - 1][j - 1] + get_score(seq1[i-1], seq2[j-1])
            delete = M[i - 1][j] + gap_penalty
            insert = M[i][j - 1] + gap_penalty
            M[i][j] = max(match, delete, insert)

    # Trace back to build the aligned sequences and track the path
    aligned_seq1, aligned_seq2 = "", ""
    path = []
    i, j = m, n
    while i > 0 or j > 0:
        path.append((i, j))
        if i > 0 and j > 0 and M[i][j] == M[i - 1][j - 1] + get_score(seq1[i-1], seq2[j-1]):
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            i -= 1
            j -= 1
        elif i > 0 and M[i][j] == M[i - 1][j] + gap_penalty:
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = "-" + aligned_seq2
            i -= 1
        else:
            aligned_seq1 = "-" + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            j -= 1
    path.append((0, 0))  # Add the starting point

    return M, M[m][n], aligned_seq1, aligned_seq2, path

# Usage
nucleotides = ['A', 'C', 'G', 'T']
seq1 = ''.join(random.choice(nucleotides) for _ in range(100))
seq2 = ''.join(random.choice(nucleotides) for _ in range(100))

matrix, score, aligned_seq1, aligned_seq2, path = nw(seq1, seq2)
print(f"Optimal Alignment Score: {score}")
print(f"Aligned Sequence 1: {aligned_seq1}")
print(f"Aligned Sequence 2: {aligned_seq2}")

# Plot heatmap
mat = np.array(matrix)
sns.set_style("whitegrid")
plt.figure(figsize=(12, 10))
sns.heatmap(mat, annot=False, cmap="Reds", linewidths=0.5, linecolor="lightgray")

# Plot path
for i in range(len(path) - 1):
    x1, y1 = path[i]
    x2, y2 = path[i + 1]
    plt.plot([y1, y2], [x1, x2], 'b-', linewidth=2)

plt.xlabel('Sequence 2')
plt.ylabel('Sequence 1')
plt.title('Needleman-Wunsch Alignment')
plt.show()
