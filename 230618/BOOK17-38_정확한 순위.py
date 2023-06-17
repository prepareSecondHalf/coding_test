# 선생님은 시험을 본 학생 N명의 성적을 분실하고 성적을 비교한 결과의 일부만 갖고 있다.
# 학생 N명의 성적은 모두 다르다.
# 1번 성적 < 5번 성적
# 3번 성적 < 4번 성적
# 4번 성적 < 2번 성적
# 4번 성적 < 6번 성적
# 5번 성적 < 2번 성적
# 5번 성적 < 4번 성적
# A번 학생의 성적이 B번 학생의 성적보다 낮다면 A => B로 표시된다.
# 이를 통해 순위 유추가 가능한 경우가 있다.
# 성적 순위를 정확히 알 수 있는 학생은 모두 몇 명인지 계산하는 프로그램을 작성하시오

# 입력
# 첫째 줄에 학생의 수 N(2<=N<=500), 성적을 비교한 횟수 M(2<=M<=10000)이 주어진다.
# 다음 M개의 줄에 두 학생의 성적을 비교한 결과를 나타내는 양의 정수 A, B가 주어진다.
# 이는 A의 점수가 B보다 낮다는 것을 의미한다.

# 출력
# 첫째 줄에 성적 순위를 정확히 알 수 있는 학생 수를 출력한다.

# 풀이
# 경로가 존재하는지를 찾으라는 뜻.
# 플로이드 워셜로 그래프를 그리고 INF가 아닌 애들의 개수를 출력하면 된다.

# 테스트 케이스
# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4

import sys

n, m = map(int, sys.stdin.readline().split())

# graph 초기화(경로가 있으면 1, 없으면 INF)
INF = float("inf")
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 주어진 케이스 입력
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1

# 자기 자신과 비교할 수 없으므로 0
for i in range(1, n + 1):
    graph[i][i] = 0

# 플로이드 워셜로 거쳐서 갈 수 있는 경우 graph에 입력
for v in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][v] + graph[v][b], graph[a][b])
print(*graph, sep="\n")

# a => b, b => a가 전부 INF면 알 수 없는 케이스
result = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            # 타겟 학생(i)이 비교 대상 학생(j)과 비교 가능하다면 i와 비교 가능한 학생수(count) 체크
            count += 1
    if count == n:
        # 비교 가능한 학생 수(count)가 전체 학생 수(n)와 같으면 정확한 순위를 알 수 있다는 것
        result += 1
print(result)
