def find_parent(parent, x):
  if (parent[x] != x):
    return find_parent(parent, parent[x])
  return parent[x]


def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
edges = []
result = 0

for _ in range(m):
  x, y, z = map(int, input().split())
  edges.append((z, x, y))

edges.sort()
total = 0

for edge in edges:
  cost, a, b = edge
  total += cost
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(total - result)
'''
* 이 문제에서는 가로등이 켜진 도로만을 이용해서, 모든 두 집이 서로 도달이 가능해야 한다는 조건을 제시하고 있다. 이때 최소한의 비용으로 모든 집을 연결해야 하기 때문에, 이를 통해 전형적인 최소 신장 트리 문제라는 것을 알 수 있다.
* 주어진 입력을 통해서 그래프를 구성한 뒤에 크루스칼 알고리즘을 수행하면 된다.
* 문제에서 요구하는 답은 '절약할 수 있는 최대 금액'이므로 '전체 가로등을 켜는 비용 - 최소 신장 트리를 구성하는 비용'을 출력한다.
'''
