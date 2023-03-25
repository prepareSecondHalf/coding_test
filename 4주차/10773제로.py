import sys

k = int(sys.stdin.readline())
number = []


for i in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        number.pop() #number의 마지막 요소를 제거
    else:
        number.append(n)

print(sum(number))