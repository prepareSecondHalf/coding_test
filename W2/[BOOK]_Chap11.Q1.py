n = 6
str = '6 4 3 3 3 3 2'
list = list(map(int, str.split()))
list.sort(reverse=True)

res = 0
cnt = 0

for i in range(n):
  if cnt >= list[i]:
    res += 1
    cnt = 0
  cnt += 1

print(res)