n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
  print('\ni : ', i)
  for j in range(i):
    print('j : ', j)
    if arr[i] < arr[j]:
      print('< : ', arr[i], arr[j])
      dp[i] = max(dp[i], dp[j] + 1)
      print('dp : ', dp)

print(len(arr) - max(dp))

# a[i]의 값이 더 작은 경우에 dp의 값을 배정해 줬다는 것이다. 그 이유는 여기에서는 증가하는 부분수열이아니라 감소하는 부분수열이기 때문이다.
# 여기에서 우리가 구해야하는 것은, 최대 부분수열의 길이가 아니라 전체에서 최대 부분수열의 길이만큼 빼준 값이기 때문에 대상이 되는 리스트 a의 길이에서 감소하는 최대 부분수열의 길이만큼을 빼준 값이 정답이 된다.