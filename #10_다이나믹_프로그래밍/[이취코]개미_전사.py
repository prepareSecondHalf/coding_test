# 내가 작성한 코드

n = int(input())
arr = list(map(int, input().split()))

'''
  > 홀수 인덱스 탐색
  > 짝수 인덱스 탐색
  각 경우의 합을 비교하여 큰 값을 출력
'''
leftSum = 0
for i in range(0, n, 2):
  leftSum += arr[i]

rightSum = 0
for i in range(1, n, 2):
  rightSum += arr[i]

print(max([leftSum, rightSum]))

# 풀이 소스코드
n = int(input())
arr = list(map(int, input().split()))

# DP 테이블 초기화
d = [0] * 100

# 보텀업 방식
d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(2, n):
  d[i] = max(d[i - 1], d[i - 2] + arr[i])

print(d[n - 1])