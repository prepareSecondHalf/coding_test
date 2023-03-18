import sys

N = int(sys.stdin.readline())
datas = []

# 전체 입력
for i in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    datas.append((x, y))
    
# 모든 사람들에 대해
for data in datas:
    # 현재 사람보다 덩치가 작은 사람만 가져와서
    comp = [x for x in datas if data[0] < x[0] and data[1] < x[1]]
    
    # + 1한 결과값 출력(최소 1등이니까)
    print(len(comp) + 1, end=' ')