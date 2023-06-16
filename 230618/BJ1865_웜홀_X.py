# 때는 2020년, 백준이는 월드나라의 한 국민이다. 
# 월드나라에는 N개의 지점이 있고 N개의 지점 사이에는 M개의 도로와 W개의 웜홀이 있다. 
# (단 도로는 방향이 없으며 웜홀은 방향이 있다.) 
# 웜홀은 시작 위치에서 도착 위치로 가는 하나의 경로인데, 특이하게도 도착을 하게 되면 시작을 하였을 때보다 시간이 뒤로 가게 된다. 
# 웜홀 내에서는 시계가 거꾸로 간다고 생각하여도 좋다.

# 시간 여행을 매우 좋아하는 백준이는 한 가지 궁금증에 빠졌다. 
# 한 지점에서 출발을 하여서 시간여행을 하기 시작하여 다시 출발을 하였던 위치로 돌아왔을 때, 
# 출발을 하였을 때보다 시간이 되돌아가 있는 경우가 있는지 없는지 궁금해졌다. 
# 여러분은 백준이를 도와 이런 일이 가능한지 불가능한지 구하는 프로그램을 작성하여라.

# 입력
# 첫 번째 줄에는 테스트케이스의 개수 TC(1 ≤ TC ≤ 5)가 주어진다. 
# 그리고 두 번째 줄부터 TC개의 테스트케이스가 차례로 주어지는데 
# 각 테스트케이스의 첫 번째 줄에는 지점의 수 N(1 ≤ N ≤ 500), 도로의 개수 M(1 ≤ M ≤ 2500), 웜홀의 개수 W(1 ≤ W ≤ 200)이 주어진다. 
# 그리고 두 번째 줄부터 M+1번째 줄에 도로의 정보가 주어지는데 각 도로의 정보는 S, E, T 세 정수로 주어진다. 
# S와 E는 연결된 지점의 번호, T는 이 도로를 통해 이동하는데 걸리는 시간을 의미한다. 
# 그리고 M+2번째 줄부터 M+W+1번째 줄까지 웜홀의 정보가 S, E, T 세 정수로 주어지는데 S는 시작 지점, E는 도착 지점, T는 줄어드는 시간을 의미한다.
# T는 10,000보다 작거나 같은 자연수 또는 0이다.
# 두 지점을 연결하는 도로가 한 개보다 많을 수도 있다. 지점의 번호는 1부터 N까지 자연수로 중복 없이 매겨져 있다.

# 출력
# TC개의 줄에 걸쳐서 만약에 시간이 줄어들면서 출발 위치로 돌아오는 것이 가능하면 YES, 불가능하면 NO를 출력한다.

import sys

# 풀이: 음으로 갈 수 있으므로 플로이드 워셜
tc = int(sys.stdin.readline())

# 테스트 케이스 1
# n:  3     m:  3     w:  1
# s:  1     e:  2     t:  2
# s:  1     e:  3     t:  4
# s:  2     e:  3     t:  1
# ws: 3     we: 1     wt: 3

for i in range(tc):
    n, m, w = map(int, sys.stdin.readline().split())
    print('case', i)

    # graph 초기화
    INF = float('inf')
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j: graph[i][j] = 0

    # 도로
    for j in range(1, m+1):
        s, e, t = map(int, sys.stdin.readline().split())
        # 테이블에 도로 정보 업데이트(방향이 없으므로 s>e === e>s)
        graph[s][e] = min(graph[s][e], t)
        graph[e][s] = min(graph[e][s], t)
    print(*graph, sep='\n')
    # 여기까지 하면 일반적인 플로이드 워셜 그래프가 완성됨
    # 0 2 4
    # 2 0 1
    # 4 1 0

    # 웜홀: 웜홀 타고 가면 시간이 마이너스로 간다!
    # 웜홀을 탔을 때를 찾아야 하므로 기존 도로 정보를 웜홀로 대체
    for j in range(1, w+1):
        s, e, t = map(int, sys.stdin.readline().split())
        graph[s][e] = -t
    print('웜홀 적용 후')
    print(*graph, sep='\n')
    # 웜홀 적용 후 이렇게 -가 포함된 테이블이 완성됨
    # 0 2 4
    # 2 0 1
    # -3 1 0

    # 플로이드 워셜로 최단 거리를 갱신
    for v in range(1, n+1):
        for s in range(1, n+1):
            for e in range(1, n+1):
                if s == e: continue
                graph[s][e] = min(graph[s][e], graph[s][v]+graph[v][e])
    print('최단 거리 갱신')
    print(*graph, sep='\n')
    # 웜홀 때문에 -인 최단 거리가 아래와 같이 생김
    #  0     2     3
    # -2     0     1
    # -3    -1     0

    # start => via => start를 했을 때 최종적으로 걸린 시간이 -인 케이스가 있으면 YES, 없으면 NO 출력
    result = "NO"
    for v in range(1, n+1):
        for s in range(1, n+1):
            if graph[s][v] + graph[v][s] < 0:
                result = "YES"
                break
    print(result)
# 예상은 했지만 시간 초과! => 벨만-포드 알고리즘이라고 함