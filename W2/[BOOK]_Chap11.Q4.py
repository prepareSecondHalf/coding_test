n = 5
# arr = [3, 2, 1, 1, 9, 1]
arr = [1, 2, 5]

num = 1
arr.sort()

for i in arr:
  if num < i: break

  num += i

print(num)