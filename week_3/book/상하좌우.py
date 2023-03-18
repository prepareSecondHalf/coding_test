import sys

# 내 정답
N = int(sys.stdin.readline())
paths = list(map(str, sys.stdin.readline().strip().split()))

x = 1
y = 1

for path in paths:
    if path == 'L':
        if y - 1 >= 1:
            y -= 1
    elif path == 'R':
        if y + 1 <= N:
            y += 1
    elif path == 'U':
        if x - 1 >= 1:
            x -= 1
    else:
        if x + 1 <= N:
            x += 1
            
print(x, y)

# 답안
n = int(sys.stdin.readline())
x, y = 1, 1
plans = sys.stdin.readline().strip().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
	for i in range(len(move_types)):
		if plan == move_types[i]:
			nx = x + dx[i]
			ny = y + dy[i]

	if nx < 1 or ny < 1 or nx > n or ny > n:
		continue
	x, y = nx, ny

print(x, y)