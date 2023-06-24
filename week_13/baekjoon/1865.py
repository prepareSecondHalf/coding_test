# 문제를 잘못 줬다 ㅎ...
# 다익스트라, 플로이드 워셜이 아닌 벨만-포드 라는 알고리즘을 통해 풀 수가 있다고 한다.
import sys
INF = int(1e9)
input = sys.stdin.readline


def solution(N, distance, graph):
    distance[1] = 0
    for check in range(N):
        for vertex in range(1, N+1):
            for next_vertex, next_cost in graph[vertex]:
                if distance[next_vertex] > distance[vertex] + next_cost:
                    distance[next_vertex] = distance[vertex] + next_cost
                    if check == N-1:
                        return False
    return True


TC = int(input())
for test_case in range(TC):
    N, M, W = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)

    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S].append([E,T])
        graph[E].append([S,T])

    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S].append([E,-T])

    if solution(N, distance, graph):
        print("NO")
    else:
        print("YES")