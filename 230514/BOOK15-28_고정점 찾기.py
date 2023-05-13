# 고정점이란 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미한다.
# 하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며, 모든 원소가 오름차순으로 정렬되어 있다.
# 수열에 고정점이 있다면 고정점을 출력하고, 없으면 -1을 출력하는 프로그램을 작성하시오.
# 고정점은 최대 1개만 존재한다.

# 첫째 줄에 N이 입력된다. (1 <= N <= 1,000,000)
# 둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력된다. (-10^9 <= 원소 <= 10^9)

# 고정점을 출력한다.

import sys
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end)//2

        if mid == array[mid]: # mid와 target인 array[mid]가 일치하면 반환
            return mid
        elif mid < array[mid]: # target인 array[mid]가 더 크면 mid 오른쪽 탐색
            end = mid - 1
        elif mid > array[mid]: # target인 array[mid]가 더 작으면 mid 왼쪽 탐색
            start = mid + 1
    return -1

print(binary_search(numbers, 0, n-1))