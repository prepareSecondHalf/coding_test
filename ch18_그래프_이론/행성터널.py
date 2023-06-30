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


# n, m = map(int, input().split())
n = int(input())
xlst, ylst, zlst = [], [], []
for i in range(n):
  x, y, z = map(int, input().split())
  xlst.append((x, i))
  ylst.append((y, i))
  zlst.append((z, i))
xlst.sort(); ylst.sort(); zlst.sort()

edges = []
for curList in xlst, ylst, zlst:
  for i in range(1, n):
    w1, a = curList[i - 1]
    w2, b = curList[i]
    edges.append((abs(w1 - w2), a, b))
edges.sort(reverse=True)
    
parent = [i for i in range(n + 1)]
cnt, ans = n - 1, 0
while cnt:
  w, a, b = edges.pop()
  if find_parent(parent, a) == find_parent(parent, b):
    continue
  union_parent(parent, a, b)
  cnt -= 1
  ans += w
print(ans)

'''
- 간선이 주어지지 않는 문제이므로 직접 간선을 만들어야 한다.
- 한 행성에서 다른 행성과의 모든 간선을 만들어보기엔 100,000 * 100,000 * 3, 즉 O(N^2) 정도의 연산이 소모되므로 스패닝 트리를 구성하기도 전에 시간초과가 날 것이다.
- 따라서 모든 간선을 만들어보지 않고, 선택될 가능성이 있는 간선만 구성해야 한다.
- 필자는 크루스칼로 해결했기 때문에, 따로 인접 리스트를 만들거나 하진 않을 것이다.

- 어떠한 간선이 선택받을 가능성이 있을까? 단연 x, y, z 상관없이 비용이 가장 작은 간선이 선택될 것이다.
- 그리고 비용은 절대값이기 때문에 가장 근거리에 있는 행성들을 고르는 것이 제일 비용이 적다.
- 그렇다면 x, y, z 기준으로 각각 정렬한 뒤 인접한 행성들의 비용을 구해 간선을 구성하면 될 것이다.
- 또한 정렬할 때 정점을 알아야 하므로 행성 번호를 주어 구분하도록 했다.

예제를 예로 든다면 간선 리스트는 다음과 같이 구성된다. (가중치, 행성a, 행성b)
(20, 3, 4), (11, 2, 3), (10, 1, 2), (10, 0, 1), (5, 1, 4), (4, 2, 3), (3, 4, 2), (3, 0, 1), (1, 3, 0), (1, 1, 3), (0, 3, 4), (0, 0, 1)
- 작은 것부터 pop을 할 것이므로 내림차순으로 정렬했다.

- 이제 가중치가 가장 작은 간선부터 차례대로 뽑아, 크루스칼 알고리즘을 진행한다.
- 크루스칼은 가중치가 가장 작은 간선부터 n-1 개를 뽑아 스패닝 트리를 구성하는 알고리즘이다. (n = 정점의 개수)
- 다만 크루스칼에서는 유니온 파인드를 통해 간선이 사이클을 이루는지 검사해야 한다.
- 만약 사이클을 이룬다면 현재 선택된 간선이 아무리 가중치가 적더라도 최소 스패닝 트리를 구성할 수 없으므로 버리고, 다음 간선을 다시 선택한다.
- 사이클만 검사하는 과정에서 중복된 간선도 걸러지기 때문에, 중복된 간선 선택에 대해서는 염려하지 않아도 된다.
- 이렇게 총 n-1개의 간선이 선택된다면 성공적으로 최소 스패닝 트리를 구성한 것이다.
'''
