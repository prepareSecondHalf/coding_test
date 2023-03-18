n = set(range(1, 10000))
a = 0
d = []
for i in n:
    if i < 10:
        a = i + i
        d.append(a)
    elif i >= 10:
        a = i + sum(map(int, str(i)))
        d.append(a)
result = [x for x in n if x not in d]
for j in range(len(result)):
    print(result[j])

