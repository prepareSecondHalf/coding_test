# n: 학생의 수, m: 성적을 비교한 횟수
# m개의 두 학생의 성적을 비교한결과 a b (a학생은 b학생보다 성적이 낮다)
# 출력: 성적순위를 정확하게 알수있는 학생의 수
import sys

n, m = map(int, sys.stdin.readline().split())
INF = int(10e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기자신 -> 자기자신인경우 = -1
for i in range(1, n+1):
    graph[i][i] = -1

# graph[i][j] 에서 j가 i보다 성적이 낮으면 graph[i][j]를 0을주고 graph[j][i]는 1을 준다
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b][a] = 0
    graph[a][b] = 1

# 두학생을 비교했을때 성적이 더 낮은학생보다 낮은경우 찾기, 더 높은 학생보다 높은 학생찾기
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n + 1):
            # j가 i보다 성적이 높을때 k가 j보다 성적이 높다면 k는 i보다 성적이 높다
            if graph[i][j] == 1 and graph[j][k] == 1:
                graph[i][k] = 1

            # j가 i보다 성적이 낮을때 k가 j보다 성적이 낮다면 k는 i보다 성적이 낮다
            elif graph[i][j] == 0 and graph[j][k] == 0:
                graph[i][k] = 0

cnt = n
# for문을 돌려서 graph[i]안에 INF가 있으면 cnt를 1명빼고 가장안쪽 for문을 break
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            cnt -= 1
            break
print(cnt)