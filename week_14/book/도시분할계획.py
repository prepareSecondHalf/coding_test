import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [0] * (N + 1)

edges = []
result = 0

for i in range(1, N + 1):
	parent[i] = i

for _ in range(M):
	a, b, cost = map(int, input().split())
	edges.append((cost, a, b))
        
edges.sort()

max = 0

for edge in edges:
     cost, a, b = edge

     if find_parent(parent, a) != find_parent(parent, b):
          union_parent(parent, a, b)
            # 원래 계속 비교를 통해서 했었는데
            # 생각해보니 30번째 줄에서 cost 에 따라 정렬하는게 크루스칼 알고리즘이었음 ㅋㅋ
          max = cost
          result += cost

print(result - max)