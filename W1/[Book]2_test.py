n, m = map(int, input().split())
 
res = 0
for i in range(n):
  numberList = list(map(int, input().split()))
  minNum = min(numberList)
  if minNum > res:
    res = minNum
 
print(res)