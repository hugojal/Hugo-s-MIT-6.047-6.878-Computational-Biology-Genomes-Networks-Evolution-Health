# Define cent coins in euros
c = [1, 2, 5, 10, 20, 50]
M = 99

# Greedy aproach
def greedy_change(M, c):
  c.sort(reverse = True)
  coin = []

  for i in range(len(c)): 
    while M > 0:
      if M >= c[i]:
        M = M - c[i]
        coin.append(c[i])
      else:
        break
  
  return coin

# Division
def div_change(M, c):
  c = sorted(c, reverse = True)
  coin = []

  for denomination in c:
    count = M // denomination
    coin.extend([denomination]*count)

    M%= denomination
    
  if M == 0:
      return coin
  else:
      return None
