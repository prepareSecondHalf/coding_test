# 동빈이는 N개의 동전을 가지고 있습니다.
# N개의 동전을 이용해 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램은?

# 첫째 줄에 동전의 개수를 나타내는 양의 정수 N이 주어진다.
# 둘째 줄에 각 동전의 화폐 단위를 나타내는 N개의 자연수가 주어지며 각 자연수는 공백으로 구분한다.

# 첫째 줄에 최솟값을 출력한다.

import sys
n = int(sys.stdin.readline().strip())
coins = list(map(int, sys.stdin.readline().split()))

# 풀이: 정렬한 뒤 앞에서부터 하나씩 더해 나간다.
# 이전 sum과 현재 sum을 비교해서 그 차이가 1보다 크거나
coins.sort()

prev_sum = coins[0]
curr_sum = 0
for coin in coins[1:]:
    curr_sum += prev_sum + coin
    if (curr_sum - prev_sum > 1 || )
    # 1 1 2 3 9
    # 3 5 7

