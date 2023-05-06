import sys

N = int(sys.stdin.readline())
my_arr = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline())
want_arr = list(map(int, sys.stdin.readline().strip().split()))

my_arr.sort()

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if my_arr[mid] == target:
            return my_arr[mid]
        elif target > my_arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1

for info in want_arr:
    if binary_search(info, 0, N - 1) != -1:
        print('yes', end=' ')
    else:
        print('no', end=' ')