import sys

K, N = map(int, sys.stdin.readline().strip().split())
arr = []

for _ in range(K):
    arr.append(int(sys.stdin.readline()))

# 처음에 start를 0으로 두고 했는데 이렇게 하니 mid가 0이 될 가능성이 있어버린다.
start = 1
end = max(arr)

result = 0

while start <= end:
    mid = (start + end) // 2

    cnt_of_sliced = sum([x // mid for x in arr if x >= mid])

    if cnt_of_sliced >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)