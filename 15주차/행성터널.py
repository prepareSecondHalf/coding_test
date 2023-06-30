# n: 행성의 수
# n줄동안 각n개의 행성좌표 x,y,z(3차원)
# 출력: 모든행성을 연결하는 최소비용 (행성에서 행성사이 터널비용은 두행성의 각 xyz값끼리의 차이중 최소값)
n = int(input())
planet, roads, result = [], [], []
for i in range(n):
  x, y, z = map(int, input().split())
  planet.append([x,y,z,i])

# 가까운 거리 후보들 모아두기
for i in range(3):
  # 좌표별로 정렬 (가장 가까운 행성끼리 모아두기)
  planet = sorted(planet, key=lambda x:x[i])
  for j in range(1,n):
    roads.append([planet[j-1][3], planet[j][3], abs(planet[j-1][i]-planet[j][i])])

# 거리비용 기준으로 정렬
roads = sorted(roads, key=lambda x:x[2])

# 팀 초기화
team = [i for i in range(n)]

# 연결 확인
def check_team(team, x):
  if team[x]!=x:
    return check_team(team,team[x])
  return team[x]

# 연결
def union_team(team, a, b):
  a, b = check_team(team, a), check_team(team, b)
  if a>b:
    team[a]=b
  else:
    team[b]=a

# 크루스칼
for road in roads:
  a, b, c = road
  if check_team(team, a)!=check_team(team,b):
    union_team(team, a, b)
    result.append(c)

# 총 최소 비용 출력
print(sum(result))
