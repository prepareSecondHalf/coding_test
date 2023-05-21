n = int(input())
dp = [0] * (n - 1)
for i in range(n):
  t, p = list(map(int, input().split()))
  
  # 상담 기간이 남은 근무일보다 긴 경우는 상담을 진행할 수 없으니 건너뛴다.
  if t > n - i: 
    # print(t, n, i)
    continue
  # print(dp[:i+1])
  # dp 테이블의 값을 최댓값으로 갱신하기 위해 현재 일자 이전에 진행한 상담에서 최댓값이 있을 경우 그 값을 dp 테이블에 넣어준다.
  dp[i] = max(dp[:i+1])
  # print(dp[i] + p)
  # 현재 일자에 잡힌 상담을 처리했을 경우의 이익 값과 기존 dp테이블의 값을 비교한 뒤 값을 갱신한다.
  dp[i + t] = max(dp[i] + p, dp[i + t])

print(max(dp))

# 전체 일자를 기준으로 dp 테이블을 만들고 현재 일자에서 상담을 진행했을 경우 의 값을 갱신해준다.
