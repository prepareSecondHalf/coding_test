'''
  선택된 수의 합이 최대가 되는 경로
  선택된 수의 대각선 왼쪽 또는 오른쪽 선택 가능
  삼각형 크기: n
  나머지: 정수 삼각형

  dfs와 dp의 조합인줄 알았지만ㅠㅠ
  
'''
n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))
print(n, arr)

for i in range(1, n):
  print('\ni:  ', i)
  print('\arr:  ', arr)
  for j in range(i + 1):
    print('j: ', j)
    
    if j == 0:
      print('j-1: ', j, arr[i][j], ' and ', arr[i - 1][j])
      arr[i][j] += arr[i - 1][j]
    elif j == i:
      print('j-2: ', j, arr[i][j], ' and ', arr[i - 1][j - 1])
      arr[i][j] += arr[i - 1][j - 1]
    else:
      print('j-3: ', j, arr[i - 1][j], ' and ', arr[i - 1][j - 1])
      arr[i][j] += max(arr[i - 1][j], arr[i - 1][j - 1])
print(max(arr[-1]))

