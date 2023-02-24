n = int(input())
a = list(str(input()))
b = 0
for i in range(n):
    b += int(a[i-1])
print(b)
