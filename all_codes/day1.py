#largest product
a = [-4, -2, 3, 5, -1]
prod = 1
neg = []
for i in a:
  if (i == 0):
    continue
  elif (i > 0):
    prod = prod * i
  else:
    neg.append(i)
if (len(neg) % 2 == 1):
  c = max(neg)
  print(c)
for i in neg:
  prod = prod * i
print(prod // c)
