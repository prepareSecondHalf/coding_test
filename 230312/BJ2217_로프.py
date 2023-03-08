# N(1 ≤ N ≤ 100,000)개의 로프가 있다. 이 로프를 이용하여 이런 저런 물체를 들어올릴 수 있다. 각각의 로프는 그 굵기나 길이가 다르기 때문에 들 수 있는 물체의 중량이 서로 다를 수도 있다.
# 하지만 여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다. k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.
# 각 로프들에 대한 정보가 주어졌을 때, 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성하시오. 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.

# 첫째 줄에 정수 N이 주어진다. 다음 N개의 줄에는 각 로프가 버틸 수 있는 최대 중량이 주어진다. 이 값은 10,000을 넘지 않는 자연수이다.

# 첫째 줄에 답을 출력한다.

import sys
n = int(sys.stdin.readline().strip())
max_weights = []
for idx in range(n):
    w = int(sys.stdin.readline().strip())
    max_weights.append(w)
print(max_weights)

# 풀이: 들어올릴 수 있는 물체의 최대 중량을 구하려면 견딜 수 있는 중량이 높은 로프를 최대한 많이 사용해야 한다.
# 전부 비교하면 시간 복잡도가 n^2라 안 됨
can_be_lifted = 0

for max_weight in max_weights:
    temp = []
    for compared in max_weights:
        if compared >= max_weight:
            temp.append(compared)
    current_max = max_weight * len(temp)
    if can_be_lifted < current_max:
        can_be_lifted = current_max
print(can_be_lifted)

# 풀이2: 모든 로프에 대해 각각 자신보다 크거나 같은 수의 개수를 구해 자신 * 개수 한 뒤 최대값을 내보내면 되는데...이것 자체가 이미 n^2
# 정렬을 하면 자신보다 크거나 같은 값은 자신 뒤에 있는 요소들이 되므로 될듯
# 동일한 값이 있어도 어차피 앞에서 나온 값이므로 여기는 정확하지 않아도 상관없어진다.
# 시간 복잡도 n
max_weights.sort()
can_be_lifted = []
for idx, max_weight in enumerate(max_weights):
    current_max = max_weight * (len(max_weights) - idx)
    can_be_lifted.append(current_max)
print(can_be_lifted)
result = max(can_be_lifted)
print(result)