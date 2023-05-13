# mid 기준으로 
# mid보다 크면 설치 못 함

n, c = map(int, input().split())
house = []
for _ in range(n):
  house.append(int(input()))
house.sort()

start, end = 1, house[-1] - house[0]
reuslt = 0
while start <= end:
  mid = (start + end) // 2
  cur = house[0]
  cnt = 1
  for i in range(1, n):
    if house[i] >= cur + mid:
      cur = house[i]
      cnt += 1
  if cnt >= c:
    start = mid + 1
    result = mid
  else:
    end = mid - 1

print(result)