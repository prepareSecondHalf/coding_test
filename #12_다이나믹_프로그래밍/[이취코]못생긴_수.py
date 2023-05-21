n = int(input())
dp = [False] * 100
dp[0] = True

for i in range(2, 100):
  if i % 2 == 0:
    dp[i] = True
  if i % 3 == 0:
    dp[i] = True
  if i % 5 == 0:
    dp[i] = True

print(dp)
result = [i for i in range(len(dp)) if dp[i] is True]
print(result)
print(result[n - 1])
