# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

# 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

# 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

import sys
n = int(sys.stdin.readline())

# 1부터 n까지, 1로 만들 때까지 사용되는 연산의 수를 dp 테이블에 저장
dp = [0] * (n+1)

# 초기값
dp[1] = 0

for i in range(2, n+1): # 2부터 n까지 테이블 값 정하기
    dp[i] = dp[i-1] + 1 # 기본적으로 이전 수보다 연산을 한 번 더 한다고 가정한다. (1을 빼는 경우)

    if i % 3 == 0: # i가 3으로 나눠지는 경우, dp[i]가 1을 뺀 경우인지 3으로 나눈 경우인지 더 작은 수를 찾는다.
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0: # i가 2으로 나눠지는 경우, dp[i]가 1을 뺀 경우인지 2으로 나눈 경우인지 더 작은 수를 찾는다.
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[n])