# N종류의 화폐가 있다. 화폐의 개수를 최소한으로 이용해 그 가치의 합이 M이 되도록 한다.
# 각 화폐의 사용 개수는 제한이 없다.

# 첫 번째 줄에 n, m 이 주어진다. (1<=N<=100) (1<=M<=10000)
# 이후 N개 줄에 각 화폐의 가치가 주어진다.

# 첫째 줄에 M원을 만들기 위한 최소 화폐 개수를 출력한다.
# 불가능하면 -1을 출력한다.

import sys
n, m = map(int, sys.stdin.readline().split())
currencies = []
for i in range(n):
    currency = int(sys.stdin.readline())
    currencies.append(currency)

# 풀이: 0원부터 M+1원까지 dp table에 저장
dp = [10001] * (m+1)

dp[0] = 0
for i in range(n):
    for j in range(currencies[i], m+1):
        if dp[j - currencies[i]] != 10001:
            dp[j] = min(dp[j] - currencies[i] + 1)
if dp[m] == 10001: print(-1)
else:print(dp[m])
