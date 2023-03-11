import sys
a = list(sys.stdin.readline().split("-"))

res = 0

for i in range(len(a)):
  tempA = a[i].split("+")
  tempSum = 0
  for j in range(len(tempA)):
    tempSum += int(tempA[j])
      
  if i == 0: res += tempSum
  else: res += -tempSum

print(res)