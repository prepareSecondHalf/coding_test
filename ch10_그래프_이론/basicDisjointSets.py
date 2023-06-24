# <기본적인 서로소 집합 알고리즘 소스코드>
'''
union 연산 = 합치기 연산 : 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
find 연산 = 찾기 연산 : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산

<서로소 집합 자료구조> : [합집합 연산 + 찾기 연산] 구성 (union-find 자료구조)
: 두 집합이 서로소 관계인지 확인할 수 있다는 말 = 각 집합이 어떤 원소를 공통으로 가지고 있는지를 확인할 수 있다는 말
: 트리 자료구조 이용
∴ 서로소 집합 알고리즘으로 루트를 찾기 위해서는 재귀적으로 부모를 거슬러 올라가야 한다는 점 
∵ 임의의 요소가 각 집합에 속하는지를 알아내기 위해서 (기준은 루트노드)

<서로소 집합 알고리즘>
1. union 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
  1-1. A와 B의 루트 노드인 A`, B`를 각각 찾는다.
  1-2. A`를 B`의 부모 노드로 설정한다. (if A < B)
2. 모든 union 연산을 처리할 때까지 1번 과정을 반복한다.
'''


# [find] 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x


# [union] 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


# 1. 노드의 개수와 간선(union 연산)의 개수 입력받기 (= 노드의 개수(v) 크기의 부모 테이블을 초기화)
v, e = map(int, input().split())  # v는 노드 갯수, e는 간선 갯수
parent = [0] * (v + 1) # 부모 테이블 초기화 


# 2. 부모 테이블상에서, 부모를 자기 자신으로 초기화
# (모든 원소가 자기 자신을 부모로 가지도록 설정 => 혹은 특정한 노드의 부모에 대해서만 저장 => 루트 확인을 위해 재귀적으로 부모를 거슬러 올라가서 최종적인 루트 노드를 찾아야 한다.)
for i in range(1, v + 1):
  parent[i] = i


# 3. union 연산을 각각 수행 
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

# 4. 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
  print(find_parent(parent, i), end = ' ')

print()

# 5. 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v + 1):
  print(parent[i], end= ' ')

'''
노드와 간선은 그래프 이론에서 중요한 개념입니다.

**노드**는 그래프의 기본 요소로, 종종 "정점"이라고도 불립니다. 노드는 개별적인 개체를 나타내며, 그래프에서 하나의 점으로 표현됩니다. 예를 들어, 소셜 네트워크 그래프에서 각 사용자는 하나의 노드로 표현될 수 있습니다.

**간선**은 노드들을 연결하는 선입니다. 노드와 노드 사이의 관계를 나타내며, 그래프에서 선분 또는 화살표로 표현됩니다. 간선은 노드들 간의 상호작용이나 연결성을 표현하는 데 사용됩니다. 예를 들어, 소셜 네트워크 그래프에서 친구 관계는 사용자 노드 간의 간선으로 표현될 수 있습니다.

그래프는 일반적으로 노드와 간선의 집합으로 구성되며, 이를 통해 복잡한 시스템이나 상호작용을 모델링할 수 있습니다. 그래프 이론은 네트워크 분석, 경로 탐색, 최단 경로 문제 등 다양한 분야에서 응용되며, 실제로 컴퓨터 과학, 사회과학, 운송, 전기 및 전자 공학 등 많은 분야에서 활용됩니다.
'''
