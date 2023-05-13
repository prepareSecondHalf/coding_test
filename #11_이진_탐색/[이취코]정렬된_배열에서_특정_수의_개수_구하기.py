import sys
n, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0
start, end = 0, n - 1

while start <= end:
  mid = (start + end) // 2
  if arr[mid] == x:
    for i in range(mid, -1, -1):
      if arr[i] == x:
        cnt += 1
      else: 
        break
    for j in range(mid + 1, n):
      if arr[j] == x:
        cnt += 1
      else: 
        break
    break
  if arr[mid] > x:
    end = mid - 1
  elif arr[mid] < x:
    start = mid + 1

if cnt == 0:
  print(-1)
else:
  print(cnt)





