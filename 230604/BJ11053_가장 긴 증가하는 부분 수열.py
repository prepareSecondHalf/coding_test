# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.           O   O       O       O
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

# 그것이 아니고... 유명하다는 그 문제(증가하는 부분 수열)이므로 외운대로 풀면 된다.
dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
