import sys
read = sys.stdin.readline

n = int(read())
a = list(map(int, read().split()))
b = list(map(int, read().split()))

# 가장 작은 s를 구하기 위해, a의 가장 큰 값 * b의 가장 작은 값을 구해야 한다
# 100프로 이해가 되질 않는다
a.sort()
b.sort(reverse=True)
sum = 0

for i in range(n):
  sum += (a[i] * b[i])
print(sum)


