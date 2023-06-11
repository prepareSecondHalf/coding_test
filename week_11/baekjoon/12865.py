import sys

N, K = map(int, sys.stdin.readline().strip().split())

thing = [[0, 0]]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(N):
    thing.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = thing[i][0]
        v = thing[i][1]

        # 가방에 못넣는다
        # i - 1번째 까지의 최대 가치
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            # j만큼 베낭 공간이 있을 때 이전 인덱스까지의 최대 가치랑(현재 물건을 넣지 않을 때)
            # j만큼의 베낭 공간에서 현재 아이템 무게를 뺀 만큼의 이전 인덱스까지의 최대 가치 + 현재 물건의 가치 중에서(현재 넣을 물건의 무게만큼 베낭에서 빼고, 현재 물건을 넣을 때)
            # 더 가치가 큰 거를 dp에 저장(즉, 현재 물건을 넣지 않거나, 현재 물건을 넣는 것 중 최대 가치를 저장)
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[N][K])