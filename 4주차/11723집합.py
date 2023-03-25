import sys

m = int(sys.stdin.readline())
s = []

for i in range(m):
    word = list(map(str, sys.stdin.readline().split()))
    a = word[0]

    if len(word) == 1:
        if a == 'all':
            s = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        elif a == 'empty':
            s = []
    if len(word) == 2:
        word[1] = int(word[1])
        if a == 'add' and word[1] not in s:
            s.append(word[1])
        elif a == 'remove' and word[1] in s:
            s.remove(word[1])
        elif a == 'check' and word[1] in s:
            print(1)
        elif a == 'check' and word[1] not in s:
            print(0)
        elif a == 'toggle' and word[1] in s:
            s.remove(word[1])
        elif a == 'toggle' and word[1] not in s:
            s.append(word[1])