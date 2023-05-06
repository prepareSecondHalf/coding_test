# 부품이 N개 있다.
# 각 부품은 정수 형태의 고유 번호가 있다.
# M개 종류의 부품을 대량으로 구매하려는데, 해당 부품이 모두 있는지 확인하려고 한다.
# 요청한 부품이 있으면 yes, 없으면 no를 출력한다.

# 입력
# 첫째 줄에 정수 N이 주어진다. (1 <= N <= 1000000)
# 둘째 줄에 N개의 정수가 공백으로 구분되어 주어진다. (1 <= 정수 <= 1000000)
# 셋째 줄에 정수 M이 주어진다. (1 <= M <= 100000)
# 넷째 줄에 M개의 정수가 공백으로 구분되어 주어진다. (1 <= 정수 <= 1000000)

# 출력
# 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes, 아니면 no를 출력한다.

import sys
n = int(sys.stdin.readline())
stocks = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
reqs = list(map(int, sys.stdin.readline().split()))

def check_stock(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        center = (start + end) // 2
        if data[center] < target:
            start = center + 1
        elif data[center] > target:
            end = center - 1
        else:
            return 'yes'
    return 'no'

answer = []
for req in reqs:
    is_in_stock = check_stock(req, stocks)
    answer.append(is_in_stock)
print(answer)



# 예시1
# 5
# 8 3 7 9 2
# 3
# 5 7 9

# 예시2
# 10
# 9 8 7 11 23 93 17 82 992 3
# 5
# 3 99 93 17 333
