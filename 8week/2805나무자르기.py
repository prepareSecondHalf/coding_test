# n : 나무의수, m: 가져가려는 나무의 길이
# 나무의 높이
# 출력: 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값
import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
start = 1
end = max(a)

while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in a:
        if i >= mid:
            result += i - mid

    if result >= m:
        start = mid + 1
    else:
        end = mid -1
print(end)
