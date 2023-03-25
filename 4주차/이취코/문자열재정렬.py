import sys

n = list(sys.stdin.readline().strip())
asc_n = []
numbers = []

for i in n:
    asc_n.append(ord(i))

asc_n.sort()

for j in range(len(asc_n)):
    if asc_n[j] >= 48 and asc_n[j] <= 57:
        numbers.append(int(chr(asc_n[j])))
        asc_n[j] = int(chr(asc_n[j]))
    else:
        asc_n[j] = chr(asc_n[j])

asc_n = [x for x in asc_n if x not in numbers]
asc_n.append(sum(numbers))
for k in asc_n:
    print(k, end='')