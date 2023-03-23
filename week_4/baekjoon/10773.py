import sys

N = int(sys.stdin.readline())

result = []

for i in range(N):
    K = int(sys.stdin.readline())

    if K == 0:
        result.pop()
    else:
        result.append(K)

print(sum(result))