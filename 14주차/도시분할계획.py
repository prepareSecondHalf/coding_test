# 백준 1647
# n: 집의 개수, m: 길의 개수
# m줄에 걸쳐 길의 정보 a b:집번호, c는 비용
# 출력: 마을을 둘로 나눌때 길을 없애서 유지비의 합을 최소화 할수있는 방법
# (한 마을안에 임의의 마을 두개는 반드시 이동이 가능해야함, 마을끼리는 연결되있지 않아도된다)
import sys

# x와 연결되어있는마을중 가장 번호가작은걸 찾을때까지 재귀함수 실행
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]
# a와 연결된 마을중 가장 번호가 작은 마을과 b와 연결된 마을중 가장 번호가 작은 마을을 비교 큰마을에 작은마을번호로 교체
def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())

parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i


graph = []
for _ in range(M):
    graph.append([int(x) for x in sys.stdin.readline().rstrip().split()])

# 비용기준 정렬
graph.sort(key = lambda x:x[2])

result = 0
max_cost = 0

# 비용이 낮은 도로부터 확인하면서 연결이 안되어있을경우에만 적용해준다
for edge in graph:
    start, end, cost = edge
    # parent에서 연결되어있지않으면 result에 cost를 더해주고 max_cost에 cost최대값을 갱신해준다
    if find_parent(start) != find_parent(end):
        union(start, end)
        result += cost
        max_cost = max(cost, max_cost)

# 비용 총합 - 가장높은 비용 (가장 높은비용을 제거해서 마을두개로 나누어준다)
print(result - max_cost)