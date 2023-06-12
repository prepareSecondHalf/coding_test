# https://www.acmicpc.net/problem/11404

# n(2 ≤ n ≤ 100)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다. 
# 각 버스는 한 번 사용할 때 필요한 비용이 있다.
# 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 도시의 개수 n이 주어지고 둘째 줄에는 버스의 개수 m이 주어진다. 
# 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 
# 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 
# 버스의 정보는 버스의 시작 도시 a, 도착 도시 b, 한 번 타는데 필요한 비용 c로 이루어져 있다. 
# 시작 도시와 도착 도시가 같은 경우는 없다. 비용은 100,000보다 작거나 같은 자연수이다.
# 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.

# 출력
# n개의 줄을 출력해야 한다. i번째 줄에 출력하는 j번째 숫자는 도시 i에서 j로 가는데 필요한 최소 비용이다. 
# 만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.

# 플로이드 워셜 이차원 배열을 만들고 이걸 출력하라는 뜻!
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# 아래와 같은 케이스에서 최솟값을 갱신해 나가면서 table을 생성하면 된다.
# from: 1   to: 2   cost: 2
# from: 1   to: 3   cost: 3
# from: 1   to: 4   cost: 1
# from: 1   to: 5   cost: 10
# from: 2   to: 4   cost: 2
# from: 3   to: 4   cost: 1
# from: 3   to: 5   cost: 1
# from: 4   to: 5   cost: 3
# from: 3   to: 5   cost: 10
# from: 3   to: 1   cost: 8
# from: 1   to: 4   cost: 2
# from: 5   to: 1   cost: 7
# from: 3   to: 4   cost: 2
# from: 5   to: 2   cost: 4

# table 초기화 (출발지 == 목적지인 케이스는 0, 나머지는 INF)
INF = float('inf')
table = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j: table[i][j] = 0

# 주어진 케이스대로 a => b로 가는 경우의 cost 입력
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    table[a][b] = min(table[a][b], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            table[a][b] = min(table[a][b], table[a][k] + table[k][b])
for i in range(1, n+1):
    print(*table[i][1:], sep=" ")