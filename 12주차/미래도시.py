# n: 회사의 개수, m: 경로의 개수
# 2 ~ m+1줄까지 연결된 두 회사의 번호
# x: 가야하는 회사의 번호, k:거쳐가야하는 회사의 번호 (m+2번째줄)
# 문제: 1부터 k회사를 갔다가 x회사로 가는 최단거리를 구하시오
# 출력: 1부터 k번 회사를 갔다가 x번 회사로 가는 최소 이동 시간(불가시 -1을 출력)
import sys

n, m = map(int, sys.stdin.readline().split())
node = [[int(1e9)] * (n+1) for _ in range(n+1)] 
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    # start부터 end까지 이어져있으므로 1로바꿔준다
    node[start][end] = 1
    node[end][start] = 1

# 현재좌표에서 현재좌표까지의 거리는 0
for i in range(n):
    for j in range(n):
        if i == j:
            node[i][j] = 0

x, k = map(int, sys.stdin.readline().split())


for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            # 현재까지 찾아낸 a부터 b까지의 거리와 i를 거쳐 갈수있는 a부터b까지의 거리중 작은값을 넣어준다
            node[a][b] = min(node[a][b], node[a][i] + node[i][b])

result = node[1][k] + node[k][x]

if result >= 1e9:
    print('-1')
else:
    print(result)



