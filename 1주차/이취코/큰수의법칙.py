# 1. 첫째 줄에 N(2 <= N <= 1,000), M(1 <= M <= 10,000), K(1 <= K <= 10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 2. 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.
# 3. 입력으로 주어지는 K는 항상 M보다 작거나 같다.

n,m,k = map(int, input().split())
num_list = list(map(int,input().split()))
num_list.sort()
count = k
a = 0
for i in range(m):
    if count > 0:
        a += num_list[n-1]
        count -= 1

    else:
        a += num_list[n-2]
        count = k

print(a)
