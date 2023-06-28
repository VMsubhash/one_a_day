'''
Given a list of possible tokens, what is the minimum number of tokens to achieve a given sum

Example 

tokens are 
10 5 2 1

And the needed sum is 158

The lowest token usage will be
15 tokens numbered 10
1 token numbered 5
1 token numbered 2
1 token numbered 1
'''

a = list(map(int, input().split()))
a.sort()
a = a[::-1]
inp = int(input())
our_sum = 0
i = 0
d = {}
while our_sum != inp:
  if (inp - our_sum < min(a)):
    our_sum -= a[i]
    d[a[i]] -= 1
    i = i + 1
  if (our_sum + a[i] > inp):
    i = i + 1
  else:
    our_sum += a[i]
    if (a[i] not in d):
      d[a[i]] = 0
    d[a[i]] += 1
print(d)
