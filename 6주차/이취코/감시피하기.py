# 백준 18428
# n: 가로 세로
# 학생: S, 선생님: T, 아무것도 존재하지 않는다면: X
# 출력: 첫째 줄에 정확히 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지의 여부(YES or No)
import sys

n = int(sys.stdin.readline())
graph = []
teacher = 0
for _ in range(n):
  data = list(sys.stdin.readline().strip().split(' '))
  teacher += data.count('T')
  graph.append(data)

# 상 하 좌 우
dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]

# 4방향 확인 함수
def check_S(x,y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 이동한 위치가 범위안에 있고 and 장애물이 설치되어있지 않을경우
    while 0<= nx < n and 0<= ny < n and graph[nx][ny] !='O':
      # 감시 가능
      if graph[nx][ny] == 'S':
        return True
      else:
        # T 나 X으면 계속 탐색
        nx += dx[i]
        ny += dy[i]
  # 감시 불가
  return False

def solution(count):
  global answer
  if count == 3:
    cnt = 0
    for i in range(n):
      for j in range(n):
        if graph[i][j] == 'T':
          if not check_S(i,j):
            cnt+=1
    # 모든 선생이 감시가 불가능할 때
    if cnt == teacher:
      answer = True
    return

  # 비어있는곳에 장애물 설치후 재귀함수 실행 3개 설치되면 감시 가능여부 리턴
  for i in range(n):
    for j in range(n):
      if graph[i][j] == 'X':
        graph[i][j] = 'O'
        count +=1
        solution(count)
        graph[i][j] = 'X'
        count -=1

answer = False
solution(0)
if answer:
  print('YES')
else:
  print('NO')
