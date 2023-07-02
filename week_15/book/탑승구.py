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

gates = int(input())
airplanes = int(input())
parent = [0] * (gates + 1)

for i in range(1, gates + 1):
    parent[i] = i

result = 0

for _ in range(airplanes):
    N = int(input())
    data = find_parent(parent, N)
    if data == 0:
        break
    union_parent(parent, data, data - 1)
    result += 1

print(result)