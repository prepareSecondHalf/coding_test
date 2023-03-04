n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

res = 0

while True:
    for i in range(k):
        if m == 0:
            break
        else:
            res += data[n-1]
            m -= 1
     
    if m == 0:
        break
    else:
        res += data[n-2]
        m -= 1
    
print(res)