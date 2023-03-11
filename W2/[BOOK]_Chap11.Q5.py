n = 8
m = 5
# arr = [1, 3, 2, 3, 2]
arr = [1, 5, 4, 3, 2, 4, 5, 2]

cnt = 0

for i in range(len(arr)):
  for j in range(i, len(arr)):
    if arr[i] != arr[j]:      
      cnt += 1

print(cnt)