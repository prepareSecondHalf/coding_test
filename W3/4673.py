arr = [i for i in range(1,10001)]

for i in range(1,10001):
    num = sum(map(int, str(i)))
    if i + num <= 10000 and i + num in arr:
        a = i + num
        arr.remove(a)
        
for i in range(len(arr)):
    print(arr[i])