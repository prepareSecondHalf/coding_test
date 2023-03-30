# 인접행렬 : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
INF = 999999999 # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
  [0, 7, 5],
  [7, 0, INF],
  [5, INF, 7]
]

print(graph)

# 인접 리스트 : 리스트로 그래프의 연결 관계를 표현하는 방식
# 행(row)이 3개인 2차원 리스트로 인접 리스트 표현
graph2 = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph2[0].append((1, 7))
graph2[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph2[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph2[2].append((0, 5))

print(graph2)
print(graph2[2])
print(graph2[2][0])
print(type(graph2[2][0]))
print(graph2[2][0][0]) # 0
print(graph2[2][0][1]) # 5
print(graph2[2][0][2]) # 에러