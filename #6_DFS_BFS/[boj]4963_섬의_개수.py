from collections import deque
import sys
input = sys.stdin.readline

def BFS(y, x):
  dy = [-1, 1, 0, 0, -1, -1, 1, 1] # y direction
  dx = [0, 0, -1, 1, -1, 1, -1, 1] # x direction
  q = deque() # bfs 자료 구조에 맞게 dequq 생성
  q.append([y, x]) # 큐에 방문 위치 추가
  field[y][x] = 0 # 전달받은 위치 정보에 대해 방문 처리
    
  while q: # 큐의 내용이 없을 때까지 무한 루프
    y, x = q.popleft() # 접근할 위치 꺼내오기 (선입선출)
    for i in range(8): # 방향 개수에 맞게 8번 탐색
      next_y = y + dy[i] # 접근할 y direction
      next_x = x + dx[i] # 접근할 x direction

      # 접근할 방향이 주어진 범위 여부 확인 및 접근 할 수 있는 상태 확인
      if 0 <= next_y < h and 0 <= next_x < w and field[next_y][next_x] == 1:
        q.append([next_y, next_x]) # 조건에 부합한 좌표 큐에 추가
        field[next_y][next_x] = 0 # 방문 처리

while True: # 수행이 종료될 때까지 무한 루프
  w, h = map(int, input().split()) # w, h 입력 받음
  field = list() # 입력 값(지도)를 저장할 리스트
    
  if w == 0 and h == 0: # w와 h가 0 일 경우, 강제종료
    break
        
  for _ in range(h): # h번만큼 순회하여 리스트에 지도 입력 값을 추가
    field.append(list(map(int, input().split())))
        
  cnt = 0 # 카운트 변수
  # 2차원 리스트 탐색을 위해 이중 for문으로 탐색
  for j in range(h): # y는 h번 탐색
    for i in range(w): # x는 w번 탐색
      if field[j][i] == 1: # 방문할 위치가 접근 가능할 경우(섬)에 대한 분기 처리
        BFS(j, i) # 접근 가능한 위치에서 다방향적으로 탐색하기 위해 인자로 방문할 위치 전달 
        cnt += 1 # 섬에 대한 카운팅
                
  print(cnt) # 각 예제 카운트 넘버 출력