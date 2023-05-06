import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))

A.sort()

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().strip().split()))

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1

for data in B:
    if binary_search(data, A) == -1:
        print(0)
    else:
        print(1)