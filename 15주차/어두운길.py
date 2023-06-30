# n: 집의 수, m: 도로의수
# m개의 도로정보 x, y: 연결된 두도로(양방향), z:유지비용
# 출력: 일부 가로등으 ㄹ비활성화하여 절약할수 있는 최대금액(집끼리는 이동이 가능해야함)
import sys

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, sys.stdin.readline().split())
road = [list(map(int, sys.stdin.readline().split())) for i in range(m)]
parent = [0] * (n+1)
result = 0 # 남겨진길들의 비용
total = 0 # 전체 비용

for i in range(n):
    parent[i] = i

road.sort( key=lambda x: x[2])

# 비용이 작은것부터 시작
for i in road:
    x, y, z = i
    total += z # 전체비용을 구하기위해 z를 더해줌
    
    #x와 y가 연결되어 있지않을경우 합쳐주고 해당비용을 result에 더해줌
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += z

# 총합 - 활성화된 가로등비용
print(total - result)




