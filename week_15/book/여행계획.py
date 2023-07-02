import sys
input = sys.stdin.readline

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

for i in range(N + 1):
    parent[i] = i

for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j] == 1:
            union_parent(parent, i + 1, j + 1)

plans = list(map(int, input().split()))

flag = True

for i in range(M - 1):
    if find_parent(parent, plans[i]) != find_parent(parent, plans[i + 1]):
        flag = False

if flag:
    print("YES")
else:
    print("NO")