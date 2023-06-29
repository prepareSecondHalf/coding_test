n, m = map(int, input().split())

result = 0

for i in range(n): 
    data = list(map(int, input.split()))
    min_value = min(data)
    result = max(result, min_value)

#  왜 작은 수를 찾아야 되냐
print(result)
