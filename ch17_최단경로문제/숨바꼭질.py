'''
 동빈이가 숨을 헛간 번호 출력

'''

from heapq import heappush, heappop

def dijkstra(x):
    q = [] # 다익스트라는 항상 동일하다! 힙이나 우선순위큐를 사용
    heappush(q, (0, x)) # (가중치, 노드)의 형태로 삽입

    field = [-1] * MAX # 가중치(여기서는 걸린 시간) 행렬 초기화
    field[x] = 0 # 시작 위치의 가중치는 항상 0

    while q:
        time, cx = heappop(q)
        if cx == k:
            return field[cx]
        

        for i in range(3): # 이동할 수 있는 위치(X - 1, X + 1, X * 2) 세 개 고려
            if i == 0:
                nx = cx - 1
            elif i == 1:
                nx = cx + 1
            else:
                nx = cx * 2

            if not 0 <= nx < MAX:   # 범위를 벗어나거나
                continue
            if field[nx] != -1 and field[nx] <= field[cx]:  # 이미 방문했고, 지금까지 걸린 시간보다 적으면 갱신 안 함
                continue

            if i < 2: # 한 칸씩 이동한 경우 1초
                heappush(q, (time + 1, nx))
                field[nx] = time + 1
            else: # 순간이동한 경우 0초
                heappush(q, (time, nx))
                field[nx] = time

    n, k = map(int, input().split())
    MAX = 100001
    print(dijkstra(n))