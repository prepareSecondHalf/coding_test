
def find_parent(parent, x):
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x

def union_team(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

n, m = map(int, input().split()) 
parent = [0] * (n + 1)

for i in range(n):
  parent[i] = i

for _ in range(m):
  type, a, b = map(int, input().split())
  if type == 0:
    union_team(parent, a, b)
  elif type == 1:
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
      print('YES')
    else:
      print('NO')