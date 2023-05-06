import sys
n = int(sys.stdin.readline())
allCards = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
targetCards = list(map(int, sys.stdin.readline().split()))

cnt = {}
for i in allCards:
  if i in cnt:
    cnt[i] += 1
  else:
    cnt[i] = 1

for i in targetCards:
  if i in cnt:
    print(cnt[i], end=" ")
  else:
    print(0, end=" ")