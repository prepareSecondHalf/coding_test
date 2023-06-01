# t: 테스트 케이스
# n: 세로길이, m: 가로길이
# 매장된 금의 개수
# 조건: m번만 이동 가능, 왼쪽열 어디서든 시작가능 이동은 오른쪽위, 오른쪽, 오른쪽아래로만 이동가능
# 출력: 테스트 케이스마다 채얻을수있는 금의 최대 크기
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    gold = []
    index = 0

    for i in range(n):
        gold.append(arr[index: index + m])
        index += m
        #[[1,3,3,2],[2,1,4,1],[0,6,4,7]]
    for j in range(1, m): # 가로이동
        for i in range(n): # 세로이동
            # 상단
            if i == 0:
                #우측, 우측하단으로 이동했을때 최대값 gold[i][j]에 갱신
                gold[i][j] = max(gold[i][j - 1] + gold[i][j], gold[i + 1][j - 1] + gold[i][j]) 
            # 하단
            elif i == n - 1:
                # 우측상단, 우측으로 이동했을때 최대값을 gold[i][j]에 갱신
                gold[i][j] = max(gold[i - 1][j - 1] + gold[i][j], gold[i][j - 1] + gold[i][j])
            # 중단
            else:
                # 우측상단, 우측, 우측하단으로 이동했을때 최대값을 gold[i][j]에 갱신
                gold[i][j] = max(gold[i - 1][j - 1] + gold[i][j], gold[i][j - 1] + gold[i][j], gold[i + 1][j - 1] + gold[i][j]) 

    ans = 0
    for i in range(n):
        ans = max(ans, gold[i][m - 1])
    print(ans)

    # 1 3 3 2
    # 2 1 4 1
    # 0 6 4 7
