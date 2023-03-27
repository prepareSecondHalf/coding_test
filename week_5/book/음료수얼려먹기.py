import sys

n, m = sys.stdin.readline().strip().split()

graph = []

for i in range(n):
	datas = list(map(int, sys.stdin.readline().strip()))
	graph.append(datas)
	
def dfs(x, y):
	if x < 0 or x >= n or y < 0 or y >= m:
		return False
	if graph[x][y] == 0:
		graph[x][y] = 1
		dfs(x + 1, y)
		dfs(x - 1, y)
		dfs(x, y + 1)
		dfs(x, y - 1)
		return True
	return False

result = 0

for i in range(n):
	for j in range(m):
		if dfs(i, j):
			result += 1
			
print(result)