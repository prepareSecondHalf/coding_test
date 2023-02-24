N, X = map(int,input().split())
b = list(map(int,input().split()))
for i in range(N):
    if b[i] < X:
        print(b[i], end=' ')