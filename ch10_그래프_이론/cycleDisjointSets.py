'''
[ 서로소 집합을 활용한 사이클 판별]
1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
1-1. 루트 노드가 서르 다르다면 두 노드에 대하여 union 연산을 수행한다.
1-2. 루트 노드가 서로 같다면 사이클이 발생한 것이다.
2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복한다.

- 간선의 개수가 E개 일 때 모든 간선을 하나씩 확인하며, 매 간선에 대하여 union 및 find 함수를 호출하는 방식으로 동작한다.
- 이 알고리즘은 간선에 방향성이 없는 무향 그래프에서만 적용 가능하다.

무방향 그래프와 양방향 그래프는 그래프 이론에서 중요한 두 가지 개념입니다.

무방향 그래프(undirected graph)는 간선이 방향을 가지지 않는 그래프입니다. 즉, 간선은 두 개의 정점을 연결하며, 이 연결은 양방향으로 이루어집니다. 예를 들어, 친구 관계를 표현하는 그래프에서 각 사람을 정점으로 나타내고, 두 사람 간의 친구 관계를 간선으로 나타낼 수 있습니다. 이 경우에는 A와 B가 친구라면, A에서 B로 가는 간선과 B에서 A로 가는 간선이 모두 존재합니다. 무방향 그래프는 대칭성을 가지며, 간선은 양쪽 방향으로 통행이 가능합니다.

반면에 양방향 그래프(bidirectional graph)는 간선이 방향을 가지는 그래프입니다. 간선은 출발 정점과 도착 정점 사이의 방향성을 가지며, 일방향으로만 통행이 가능합니다. 예를 들어, 도로 네트워크를 그래프로 표현할 때, 도시를 정점으로 나타내고 도로를 간선으로 나타낼 수 있습니다. 이 경우에는 한 도시에서 다른 도시로 가는 도로는 존재할 수 있지만, 그 반대 방향으로 가는 도로는 없을 수 있습니다.

요약하면, 무방향 그래프는 간선에 방향이 없으며 양방향으로 통행이 가능한 반면, 양방향 그래프는 간선에 방향이 있으며 일방향으로만 통행이 가능합니다.
'''

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a , b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
     