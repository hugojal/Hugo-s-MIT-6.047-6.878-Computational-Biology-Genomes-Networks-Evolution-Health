# This is a simple-logic-code I implemented while I listened to the lecture by Manolis Kellis.

# Given two strings of nucleotides:
s1 = "ATCGTACGTAAAA"
s2 = "TGCATCGAAAAAA"

# Define function
def align(s1, s2, max_shift):
  # Initialize score and shift
  max_score = 0
  best_shift = 0

  # Unless a maximum shift is set, max_shift cannot be more than the length of the smaller sequence
  if max_shift is None:
    max_shift = min(len(s1), len(s2))

  # For each shift possibility, score is set to 0 and nucleotides compared.
  for shift in range(-max_shift, max_shift+1):
      score = 0
      for i in range(len(s2)):
          try:
            if s1[i + shift] == s2[i]:
              score += 1
            else:
              score -= 0.5

          except IndexError:
            break
      # For each shift, if the score is higher than the previous highest it is updated along with the best shift
      if score > max_score:
          max_score = score
          best_shift = shift
  
  if best_shift < 0:
      # For negative shifts, add spaces at the front of s1
      aligned_s1 = ' ' * abs(best_shift) + s1

  else:
      # For positive shifts, add spaces at the end of s1
      aligned_s1 = s1[:len(s2) - best_shift]+ ' ' * best_shift

  aligned_s2 = s2

  return {'Score':max_score,
          'Shift': best_shift}, list(aligned_s1), list(aligned_s2)


result, seq1, seq2 = align(s1, s2, max_shift = None)

print(f"Score:", result['Score'])
print(f"Shift:", result['Shift'])


print(f"Sequence 1:", ''.join(seq1))
print(f"Sequence 2:", ''.join(seq2))
