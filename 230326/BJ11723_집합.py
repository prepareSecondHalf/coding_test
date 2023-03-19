# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다. 

# 첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
# 둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

# check 연산이 주어질때마다, 결과를 출력한다.

import sys
m = int(sys.stdin.readline().strip())

# 풀이: 공집합 s를 만들고 시키는대로 하자
# 두 번째 줄의 입력은 '연산 수' 형태이므로 split으로 구분하여 연산하면 됨.
# add는 set의 성격상(중복X) 계산할 수 없는 경우 무시되므로 그냥 하면 됨
# discard를 쓰면 값이 없는 경우 에러를 발생시키지 않고 넘어감
result = set()
for _ in range(m):
  print('current set: ', result)
  user_input = sys.stdin.readline().split()
  if len(user_input) == 1:
    operation = user_input[0]
  else:
    [operation, operated] = user_input
  if operation == 'add':
    result.add(int(operated))
  elif operation == 'remove':
    result.discard(int(operated))
  elif operation == 'check':
    if int(operated) in result: print(1)
    else: print(0)
  elif operation == 'toggle':
    if int(operated) in result: result.remove(int(operated))
    else: result.add(int(operated))
  elif operation == 'all':
    result = set(range(1, 21))
  elif operation == 'empty':
    result = set()