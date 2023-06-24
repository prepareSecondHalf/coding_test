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

N, M = map(int, sys.stdin.readline().strip().split())
parent = [0] * (N + 1)

for i in range(N + 1):
    parent[i] = i

for i in range(M):
    type, a, b = map(int, sys.stdin.readline().strip().split())
    if type == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
