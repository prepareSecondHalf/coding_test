import sys

a, b = map(int, sys.stdin.readline().split())
divNum = list()
res = 0

for _ in range(a):
    divNum.append(int(sys.stdin.readline()))

divNum.sort(reverse=True)

for i in range(a):
  if b//divNum[i] > 0:
    res += b//divNum[i]
    b -= divNum[i] * (b//divNum[i])

print(res)