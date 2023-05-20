# n: 병사의 수
# n명의 병사 전투력
# 출력: 병사를 열외시켜서 내림차순으로 만들시 최소한으로 열외할수있는 병사의 수
import sys

n = int(sys.stdin.readline())
a = [int(x) for x in sys.stdin.readline().split()]
dp = [1] * n

# for문을 n까지 돌리고 그안에서 다시 for문을 i까지 돌려준다
for i in range(n):
    for j in range(i):
        # a[i]가 앞에있는 전투력보다 작을경우 dp[i]와 dp[j]+1 중 큰값을 삽입
        if a[i] < a[j]: 
            dp[i] = max(dp[i], dp[j]+1)
# ex) dp = [1, 2, 3, 3, 4, 5, 5]
print(len(a) - max(dp))