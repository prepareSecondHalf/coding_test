'''
  다이나믹 프로그래밍 : 한 번 해결된 부분의 정답을 메모리에 기록하여, 한 번 계산한 답은 다시 계산하지 않도록 하는 문제 해결 기법(점화식 이용)
  - 점화식이랑 인접한 항들 사이의 관계식
  
  t = 테스트 갯수
  n * m 크기의 금광
  m번 이동 : 오른쪽, 오른쪽 위, 오른쪽 아래
  금의 최대 크기

  제공된 이차원 테이블 list화
  dp 테이블 초기화
  
  보텀업 방식 : 단순 반복문으로 작은 문제를 먼저 해결하고, 해결된 작은 문제를 모아 큰 문제를 해결하는 방식
  for _ in range(t): 
    첫번째 열에서 가장 큰 수를 구한다
    가장 큰 수를 total에 추가한다
  
  [점화식]
    위치한 열에서 이동 가능한 다음 열의 값을 파악한다
    - 단, 범위를 넘어가는 경우는 통과한다
    이동 가능한 다음 열 중 큰 값의 셀로 이동한다
    해당 셀의 값을 total에 추가한다
    이동 위치 > m 일 경우, 탐색을 종료한다

    colItems = [...]
    curr = max(colItems)
    d[i] = curr + d[i - 1]
  print(total)
'''
# table = list(map(int, sys.stdin.readline().split()))
# table = [[i, j] for i in range(n) for j in range(m)]

import sys
t = int(sys.stdin.readline())
dx = [-1, 0, 1]
dy = [1, 1, 1]

# t번 테스트
for _ in range(t):
  n, m = map(int, sys.stdin.readline().split())
  table = []
  tmpTable = list(map(int, sys.stdin.readline().split()))

  # table 초기화
  for j in range(n):
    temp = []
    for i in range(m * j, m * j + 3 + 1):
      temp.append(tmpTable[i])
    table.append(temp)

  # dp table 초기화
  dp = []

  # dp[0] 구하기
  tmp = []
  for i in range(n):
    tmp.append(table[i][0])
  dp.append(max(tmp))
  currDy = tmp.index(max(tmp))

  # [function] 탐색 가능한 셀의 값 중 가장 큰 값 찾기
  def findMax(i):
    global currDy
    tmp = [-1] * m
    
    for p in range(3):
      # nx = j + dx[p]
      nx = currDy + dx[p]
      ny = i + dy[p]

      if (nx >= 0 and nx < n and ny >= 0 and ny < m):
        tmp[nx] = table[nx][ny]
        # tmp.append(table[nx][ny])

    # 제일 큰 값의 인덱스 값 가져오기 (index 메서드는 첫번째 값만 가져옴)
    # currDy = tmp.index(max(tmp))
    big = max(tmp)
    
    for (index, item) in enumerate(tmp):
      if item == big:
        currDy = index
    dp.append(max(tmp))
    return 0

  # m - 1번 테이블 탐색
  for i in range(m - 1):
    # 이동 가능 영역 탐색
    findMax(i)
  print(sum(dp))
