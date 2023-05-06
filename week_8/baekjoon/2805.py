import sys

N, M = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

start = 0
end = max(arr)

result = 0

while start <= end:
    mid = (start + end) // 2

    sum_of_sliced = sum([x - mid for x in arr if x > mid])
    if sum_of_sliced >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)