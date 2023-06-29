'''
  1~G개의 탑승구
  P개의 비행기 - gi번째 탑승구 중 하나에 영구적 도킹 
  최대한 몇 대 도킹할 수 있는지 출력
'''
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


G = int(input())
P = int(input())
# parent = [0] * (G + 1)
parent = [i for i in range(G + 1)]
result = 0

for _ in range(P):
  gi = int(input())
  root = find_parent(parent, gi)

  if root == 0:
    break
  else:
    union_parent(parent, root, root - 1)
    result += 1

print(result)