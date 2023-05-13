# 고정점 최대 1개 존재
# 없으면 -1
# 시간 복잡도 logN에 맞추려면 어떻게 접근해야할까?
'''
  mid가 arr[mid]보다 작을 경우 => end = mid - 1
  mid가 arr[mid]보다 큰 경우 => start = mid + 1
'''
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
start = 0
end = n - 1
isExist = False
while start <= end:
  mid = (start + end) // 2
  if arr[mid] == mid:
    isExist = mid
    break
  if arr[mid] > mid:
    end = mid - 1
  elif arr[mid] < mid:
    start = mid + 1

if isExist == False:
  print(-1)
else:
  print(isExist)
  

