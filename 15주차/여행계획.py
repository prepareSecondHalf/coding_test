# n: 여행지의수, m: 여행계획에 속한 도시수
# n줄에 걸쳐 두여행지가 연결되어있는지 여부(1일경우 연결)
# 마지막줄에 가야할 여행지번호
# 출력: 여행계획이 가능하면 YES 불가능하면 NO
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


n, m = map(int, sys.stdin.readline().split())
parent = [0] * (n+1)

# 각 위치를 자기자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

for i in range(n):
    data = list(map(int, sys.stdin.readline().split())) # 연결여부
    # 연결되있는부분 연결
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i+1, j+1)

plan = list(map(int, sys.stdin.readline().split())) # 여행계획

result = True

# 가야할 여행지중에 연결되있지 않은 부분이 있으면 result를 False로 바꿔준다
for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False

if result:
    print('YES')
else:
    print('NO')


