
'''
    이 문제의 핵심 아이디어 : 전체 그래프에서 2개의 최소 신장 트리를 만드는 것
    최소 비용으로 어떻게 2개의 신장 트리로 분할할 수 있을까?
    => 크루스칼 알고리즘으로 최소 신장 트리를 찾은 뒤에 최소 신장 트리를 구성하는 간선 중에서 가장 비용이 큰 간선을 제거하는 것
    (아이디어 굿 : 도식을 보면 쉽게 이해됨)
'''
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_team(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

n, m = map(int, input().split()) # n: 집의 개수 m: 길의 개수
parent = [0] * (n + 1)
edges = []
result = 0

for i in range(1, n + 1):
  parent[i] = i

for _ in range(m):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

edges.sort()
last = 0 # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_team(parent, a, b)
    result += cost
    last = cost

print(result - last)
