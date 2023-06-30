# g: 탑승구의 수
# p: 비행기의 수
# 각 비행기가 도킹할 수 있는 탑승구의 정보
# 출력: 도킹할수있는 비행기의 최대수(탑승구당 한대 도킹)
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


g = int(sys.stdin.readline())
p = int(sys.stdin.readline())
plane = [int(sys.stdin.readline()) for _ in range(p)]

parent = [0] * (g+1) # 탑승구에 비행기가 도킹되있는지 체크하기 위함
cnt = 0

# parent요소들을 자기자신으로 초기화
for i in range(1, g+1):
    parent[i] = i
 
for i in plane:
    check = find_parent(parent, i)

    # parent[0] 제외
    if check == 0:
        break
    # 도킹이 되어있으면 그 아래껄 확인해서 도킹하고 count +1
    union_parent(parent, check, check-1)
    cnt += 1

print(cnt)


