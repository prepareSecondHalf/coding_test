import sys

n = int(sys.stdin.readline())

time = []

endTime = 0
cnt = 0

for i in range(n):
  a, b = map(int, sys.stdin.readline().split())
  time.append([a, b])

time.sort(key = lambda x:x[0])
time.sort(key = lambda x:x[1])

for i in range(n):
  if endTime <= time[i][0]:
    endTime = time[i][1]
    cnt += 1

print(cnt)