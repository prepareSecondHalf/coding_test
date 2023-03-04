n, num = map(int, input().split())
numberList = list(map(int, input().split()))

for i in numberList:
    if num > i: print(i, end=" ")