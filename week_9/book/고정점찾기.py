import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))

def binary_search(arr, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return None

result = binary_search(arr, 0, len(arr))

if result == None:
    print(-1)
else:
    print(result)