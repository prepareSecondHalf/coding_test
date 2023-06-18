'''
    n개 도시, m개 버스
    모든 도시의 쌍(a, b)에 대해서 도시 a에서 b로 가는 최소 비용

    i를 출발해 j로 바로 가는 것보다 i를 출발해 k를 거쳐 j로 가는 게 효율적일 경우(저렴할 경우) 해당 값을 갱신해주는 것이다
    bus_cost[i][j] = min(bus_cost[i][j], bus_cost[i][k] + bus_cost[k][j])

    시간 복잡도는 O(n^3)
    3중 포문 중 경로가 되는 k의 포문이 가장 위에 있어야 누락하지 않고 한번에 돌 수 있다는 것
'''

n = int(input())
m = int(input())
bus_cost = [[100001 for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    bus_cost[start][end] = min(cost, bus_cost[start][end])

for k in range(1, n+ 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                bus_cost[i][j] = 0
            else:
                bus_cost[i][j] = min(bus_cost[i][j], bus_cost[i][k] + bus_cost[k][j])

for row in bus_cost[1: ]:
    for col in row[1:]:
        if col == 100001:
            print(0, end = " ")
        else: 
            print(col, end =  " ")
    print()