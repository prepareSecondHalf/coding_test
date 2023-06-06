# 방문 판매원 A는 많은 회사가 모여 있는 공중 미래 도시에 있다.
# 공중 미래 도시에는 1번부터 N번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 통해 연결되어 있다.
# 방문 판매원 A는 현재 1번 회사에 위치해 있으며 X번 회사에 방문해 물건을 판매하고자 한다.
# 공중 미래 도시에서 특정 회사에 도착하기 위한 방법은 회사끼리 연결되어 있는 도로를 이용하는 방법이 유일하다.
# 또한 연결된 2개의 회사는 양방향으로 이동할 수 있다.
# 공중 미래 도시에서의 도로는 마하의 속도로 사람을 이동시켜 주기 때문에 특정 회사와 다른 회사가 도로로 연결되어 있다면 정확히 1만큼의 시간으로 이동할 수 있다.
# 또한 방문 판매원 A는 기대하던 소개팅에도 참석하고자 한다.
# 소개팅 상대는 K번 회사에 존재한다.
# A는 X번 회사에 가서 물건을 판매하기 전에 소개팅 상대의 회사에서 커피를 마실 예정이다.
# 즉 A는 1번 > K번 > X번으로 가는 것이 목표다.
# 가능한 빠르게 이동하고자 할 때, 회사 사이를 이동하는 최소 시간을 계산하는 프로그램을 작성하시오

# 입력
# 첫째 줄에 전체 회사의 개수 N과 경로의 개수 M이 공백으로 구분되어 주어진다. (1 <= N, M <= 100)
# 둘째 줄부터 M+1번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 주어진다.
# M+2번째 줄에는 X와 K가 공백으로 구분되어 주어진다. (1 <= K <= 100)

# 출력
# 첫째 줄에 방문 판매원 A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간을 구하라.
# 만약 X번 회사에 도달할 수 없다면 -1을 출력한다.

import sys
n, m = map(int, sys.stdin.readline().split())

# 풀이: a에서 b로 갈 때의 최단 경로를 graph에 담기
# 1. 최단 경로 graph 생성
INF = float('inf')
graph = [[INF] * (n+1) for _ in range(n+1)]
# 2. 자기 자신으로 가는 경우 초기화 => 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0
# 3. 주어진 간선 초기화(한 번에 갈 수 있는 경우) => 1(양방향 이동이 가능하고 걸리는 시간이 1이므로)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1
# ★ 여기까지의 graph를 찍어 보면 아래와 같이 주어진 간선이 모두 찍혀 있다.
print(*graph, sep="\n")
# 0     1     1     1     inf
# 1     0     inf   1     inf
# 1     inf   0     1     1
# 1     1     1     0     1
# inf   inf   1     1     0
# 4. 이제 1=>5, 2=>3, 2=>5, 3=>2, 5=>1, 5=>2로 가는 길이 안 나와 있으므로 걔네를 찾아서 graph에 넣어 두면 된다.
# 여기서는 어디든 걸리는 시간이 1이라 아마 갱신 케이스가 없을 것 같지만
# (시작점 a, 도착점 b, 경유지 c인 경우)
# a => b로 바로 가는 경우에 걸리는 시간 vs a => c => b로 c를 거쳐 가는 경우에 걸리는 시간
# 을 비교해 최솟값을 넣으면 된다.
for c in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])
# ★ 여기까지의 graph를 찍어 보면 아래와 같이 모두 찍히게 된다.
# 0  1  1  1  2
# 1  0  2  1  2
# 1  2  0  1  1
# 1  1  1  0  1
# 2  2  1  1  0
print(*graph, sep="\n")
# 5. 1 => k => x로 가는 케이스를 graph에서 찾아 조건에 맞게 출력하면 된다.
x, k = map(int, sys.stdin.readline().split())
distance = graph[1][k] + graph[k][x]
if distance >= INF: print(-1)
else: print(distance)

# TEST CASE1
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
# 출력: 3

# TEST CASE2
# 4 2
# 1 3
# 2 4
# 3 4
# 출력: -1
