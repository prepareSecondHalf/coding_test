import sys

n = int(sys.stdin.readline())
count = n
for i in range(n):
    group = list(sys.stdin.readline())
    for j in range(0, len(group)-1):
        if group[j] == group[j+1]:
            pass
        elif group[j] in group[j+1:]:
            count -= 1
            break
print(count)

