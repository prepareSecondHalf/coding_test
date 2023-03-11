import sys

N = int(sys.stdin.readline())

info = []

for i in range(N):
    start, end = map(int, sys.stdin.readline().strip().split())
    info.append((start, end))
    
info = sorted(info, key=lambda x: (x[1], x[0]))

current_meeting = info[0]
cnt = 1

for i in range(1, N):
    if info[i][0] >= current_meeting[1]:
        cnt += 1
        current_meeting = info[i]

print(cnt)