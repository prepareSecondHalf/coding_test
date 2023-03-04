n, k = map(int, input().split())
res = 0

while n > 0:
    if n % k == 0 :
        n = n // k
        res += 1

    else:
        n -= 1
        res += 1

    if n == 1 : break

print(res)