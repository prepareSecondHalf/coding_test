# t: 테스트 케이스의 수
# n: 지점의 수, m: 도로의 수, w: 웜홀의 수
# m개의 도로정보(s,e: 연결된 두 도로의 번호, t: 걸리는 시간)
# w개의 웜홀정보(s,e: 연결된 두 도로의 번호, t: 줄어드는 시간)
# 출력: t개의 줄에 걸쳐서 시간이 줄어들면서 출발위치로 돌아오는것이 가능하면 yes 아니면 no
import sys

t = int(sys.stdin.readline())
INF = int(10e9)

def bellman_ford(start,n):
    dist = [INF for i in range(n + 1)]
    dist[start] = 0
    # 도시마다 for문을 돌리고 그안에서 도로들을 확인한다
    for i in range(n):
        for s,e,t in graph:
            if dist[e] > dist[s] + t: # 웜홀이 있을경우 걸리는 시간을 삽입
                if i == n - 1: # i가 마지막이면 True 리턴
                    return True
                dist[e] = dist[s] + t
    return False

for _ in range(t):
    n, m, w = map(int, sys.stdin.readline().split())
    graph = []
    # 도로 정보 받기(양방향)
    for i in range(m):
        s, e, t = map(int, sys.stdin.readline().split()) # 시작, 끝, 시간
        graph.append((s, e, t))
        graph.append((e, s, t))

    # 웜홀 정보 받기(단방향)
    for i in range(w):
        s, e, t = map(int, sys.stdin.readline().split())
        graph.append((s, e, -t))

    if bellman_ford(1, n):
        print('YES')
    else:
        print('NO')