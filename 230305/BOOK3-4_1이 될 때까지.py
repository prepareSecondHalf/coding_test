# 어떤 수 N이 1이 될 때까지 두 과정 중 하나를 반복적으로 선택하여 수행한다.
# 1. N에서 1을 뺀다.
# 2. N이 K로 나누어떨어지면 N을 K로 나눈다.
# 위 규칙에 따라 N과 K가 주어질 때, 1될 때까지 수행해야 하는 최소 연산 횟수를 구하시오
# 첫 번째 줄에 N(2<=N<=100000), K(2<=N<=100000)가 공백으로 구분되어 주어진다. N>K
# 첫째 줄에 N이 1이 될 때까지 수행해야 하는 연산의 최소 횟수를 출력한다.

# 풀이1 => 시키는대로 함
import sys
n, k = map(int, sys.stdin.readline().split())
times = 0
while n != 1:
    times += 1
    if n % k == 0:
        n /= k
    else:
        n -= 1
    print('how many times? ', times, '회, n: ', int(n))
print(times)


# 풀이2 => 일단 k로 나눈다. 
# 나머지가 곧 더하는 횟수가 되므로 여기에 1(나눈 횟수)을 더하면 1회차 계산 횟수가 된다.
# n은 몫으로 해서 n == 1이 될 때까지 계산한다.
# 단, 몫이 0이 되면 안 되므로... n이 k보다 크거나 같을 때만 이렇게 계산 가능하다.
# 루프를 나왔을 때, n == 1이라면 그냥 times를 보내면 되고 k > n > 1라면 times + n - 1을 하면 된다.
# 장점: 여기도 반복문이 들어가기는 하지만 위 케이스는 times를 하나씩 세는데에 반해 한 번에 많은 횟수를 세므로 시간 절약이 될 것...아마
n, k = map(int, sys.stdin.readline().split())
times = 0
while n >= k:
    times += (n % k) + 1
    n //= k
    print('how many times? ', times, '회, n: ', int(n))
if n != 1:
    times += n - 1
print(times)


# 단순 답안 예시
n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n // k
    result += 1
while n > 1:
    n -= 1
    result += 1
print(result)

# 모범 답안 예시
# target = n보다 작은 수 중 k로 나누어 떨어지는 가장 큰 수
# 즉, n - target은 n을 k로 나눴을 때 나누어 떨어지는 수까지 -1씩 계산한 횟수가 됨
# 이후 n을 target으로 업데이트하고 횟수 1 추가, n을 k로 나눈 몫으로 업데이트
# n이 k보다 작아질 때까지(몫 1 이상 유지) 반복
# 남은 n이 1이 될 때까지 result 업데이트
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k
result += n - 1
print(result)