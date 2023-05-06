# n개의 랜선 (필요한 랜선의 개수)
# k개의 랜선 (가지고 있는 랜선의 개수)
# n개의 랜선을 얻기 최대 랜선의 길이를 구하는 프로그램


import sys
k, n = map(int, sys.stdin.readline().split())
arr = []

for i in range(k):
  arr.append(int(input()))

start = 1
end = max(arr)

while start <= end:
  mid = (start + end) // 2
  cnt = 0
  for i in range(k):
    cnt += arr[i] // mid
  if cnt >= n:
    start = mid + 1
  else:
    end = mid - 1
print(end)

