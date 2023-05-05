# 첫 시도
# 최소치 M만큼 떡을 가져가기 위한 최소 절단기 높이 구하기
def getLeastNums(array, standard):
  nums = [x - standard for x in array]
  return sum(nums)

def binary_search(target, array, start, end):
  while start <= end:
    mid = (start + end) // 2
    
    if array[mid] > start:
      end = mid - 1
    elif array[mid] < mid:
      start = mid + 1
    else:
      return mid
    
  return None

import sys
N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

for i in range(array[0], array[-1] + 1):
  result = binary_search(array, i, 0, len(array) - 1)


# 최종 코드
'''
  최대한 덜 잘랐을 경우에 대한 부분의 이해가 부족
  -> total의 크기를 작은 total이 아닌 큰 total에서 작은 total 방향으로 동작하기 때문에 
  자연스럽게 else 구문에 들어가서 최대한 덜 잘랐을 경우를 구할 수 있다

  end를 max(array)한 이유
  -> ????????

'''
import sys
N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(array)

result = 0
while start <= end:
  total = 0
  mid = (start + end) // 2

  for x in array:
    if x > mid:
      # 잘랐을 때의 떡의 양
      total += x - mid
  # 떡의 양이 부족한 경우 : 더 많이 자르기
  if total < M:
    end = mid - 1
  # 떡의 양이 충분한 경우 : 덜 자르기
  else:
    result = mid # 최대한 덜 잘랐을 경우가 정답이므로, 여기서 result 기록 ?????????
    start = mid + 1

print(result)
    
