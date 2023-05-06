# 첫번째 시도: 시간 초과
# 나무 M미터
# 목재절단기 높이 H미터 기준 - 한 줄 연속해있는 나무 모두 절단
# 적어도 M미터 나무를 가져가기 위한 절단기 높이 설정할 수 있는 높이 최댓값 구하기

import sys
# n: 나무의 수, m: 필요한 나무의 길이
n, m = map(int, sys.stdin.readline().split())
# 나무의 높이
trees = list(map(int, sys.stdin.readline().split()))
trees.sort(reverse=True)

start = 0
end = max(trees)
result = 0
while start <= end:
  total = 0
  mid = (start + end) // 2
  for tree in trees:
    if tree > mid:
      total += tree - mid

  # 가져가는 나무의 양이 적을 경우
  if total < m:
    end = mid - 1
  else:
    result = mid
    start = mid + 1
  
print (result)


# 두번째 시도: 통과
# 나무 M미터
# 목재절단기 높이 H미터 기준 - 한 줄 연속해있는 나무 모두 절단
# 적어도 M미터 나무를 가져가기 위한 절단기 높이 설정할 수 있는 높이 최댓값 구하기

import sys
# n: 나무의 수, m: 필요한 나무의 길이
n, m = map(int, sys.stdin.readline().split())
# 나무의 높이
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)
result = 0
while start <= end:
  total = 0
  mid = (start + end) // 2
  for tree in trees:
    if tree > mid:
      total += tree - mid

  # 가져가는 나무의 양이 적을 경우
  if total < m:
    end = mid - 1
  else:
    result = mid
    start = mid + 1
  
print (result)