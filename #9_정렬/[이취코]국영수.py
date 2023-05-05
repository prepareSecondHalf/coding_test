import sys
n = int(sys.stdin.readline())
array = list()

while len(array) < n:
  name, k, e, m = sys.stdin.readline().split()
  array.append([str(name), int(k), int(e), int(m)])

# 람다식을 이용한 2차원 리스트 정렬
''' 
- 마이너스만 붙여주면 내림차순으로 만들 수 있다 
- 요소가 여러개일 경우 각 요소마다 정렬기준을 정해줄 수 있다
'''
sorted_array = sorted(array, key=lambda x : (-x[1], x[2], -x[3], x[0]))

for x in sorted_array:
  print(x[0])
