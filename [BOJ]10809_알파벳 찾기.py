t = input()
aList = [chr(i) for i in range(97, 123)]
alphabetIdx = []

for i in aList:
    if i not in t:
        alphabetIdx.append(-1)
    elif i in t:
        alphabetIdx.append(t.find(i))

print(*alphabetIdx)