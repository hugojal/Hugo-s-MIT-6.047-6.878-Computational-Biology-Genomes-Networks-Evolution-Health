import pandas as pd
import numpy as np
import random

# Create the motif array and its probabilities per nucleotide and position
motif = [['A', 0.6, 0.25, 0.10, 1.0],
 ['G', 0.4, 0.25, 0.10, 0.0],
 ['T', 0.0, 0.25, 0.40, 0.0],
  ['C', 0.0, 0.25, 0.40, 0.0]]

motif = pd.DataFrame(motif)

# Extract nucleotides and probabilities
nucl = motif.iloc[:, 0]
probs = motif.iloc[:, 1:]

# Transpose the probabilities to use them as weights
probs = np.array(probs)
probs = np.transpose(probs)
probs

# Generate weigheted random sequence
s = []
for i in range(len(nucl)):
  s.append(random.choices(nucl, weights = probs[i], k=1))

# Define background probabilities
back = [['A', 0.1], ['G', 0.4], ['T', 0.1], ['C', 0.4]]

# Calculate probabilities of s coming from motif versus background; Bayes' Theorem
p = []
for i in range(len(s)):
  n = s[i][0]
  for j in range(len(probs)):
    if n == nucl[j]:
      p.append(probs[i][j])

P = (np.prod(p))
print(f"Probability for the sequence given the motif = {P}")

pb = []
for i in range(len(s)):
  n = s[i][0]
  for j in range(len(back)):
    if n == back[j][0]:
      pb.append(back[j][1])

pb = (np.prod(pb))
print(f"Probability for the sequence given the background = {pb}")

p_ms = (P*0.1)/(pb*0.9 + P*0.1)
print(f"The probability that the motif generated the sequence is:", {p_ms})
