import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().strip().split()))

M = int(sys.stdin.readline())
infos = list(map(int, sys.stdin.readline().strip().split()))

cards.sort()

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if cards[mid] == target:
            return mid
        elif cards[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

for info in infos:
    if binary_search(info, 0, N - 1) != None:
        print(1, end=' ')
    else:
        print(0, end=' ')
