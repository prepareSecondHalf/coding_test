import sys

n = list(map(str, sys.stdin.readline().strip()))
a = []
b = []

for i in range(len(n)):
    if int(len(n)/2) > i:
        a.append(int(n[i]))
    elif int(len(n)/2) <= i:
        b.append(int(n[i]))

if sum(a) == sum(b):
    print('LUCKY')
else:
    print('READY')
