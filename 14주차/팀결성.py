# n+1: 학생수 ,m: 연산의 수
# 0 a b: a가 속한팀과 b가 속한팀을 합침, 1 a b: a학생과 b학생이 같은팀에 속해있는지 확인(YES or NO)
import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
# 같은 팀 여부 확인
def find(graph, x):
    # 재귀함수로 연결되어있는 수중에 가장작은수까지 내려간다 find(graph, a) find(graph, b)로 비교했을때 같은수가 나오면 같은팀
    if graph[x] != x:
        graph[x] = find(graph, graph[x])
    return graph[x]

# 팀 합치기
def plus(graph, a, b):
    a = find(graph, a)
    b = find(graph, b)
    # 더 큰 번호를 현재 연결되어있는번호중 가장 작은번호로 바꿈
    if a < b:
        graph[b] = a
    else:
        graph[a] = b
        
for i in range(n + 1):
    graph.append(i)

for _ in range(m):
    t, a, b = map(int, sys.stdin.readline().split())
    if t == 0:
        plus(graph, a, b)
    elif t == 1:
        if find(graph, a) == find(graph, b):
            print('YES')
        else:
            print('NO')
