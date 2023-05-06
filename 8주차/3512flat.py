# n: 아파트의 방수, c: 1제곱미터당 비용
# 각 방의 면적과 유형
# 출력
# 모든 객실의 총 면적;
# 모든 침실의 총 면적;
# 아파트 비용
import sys

n, c = map(int, sys.stdin.readline().split())
home = []
a = 0 # 모든 객실의 총면적
b = 0 # 모든 침실의 총면적
cost = 0 # 아파트 비용
for _ in range(n):
    home.append(sys.stdin.readline().split())

for i in home:
    a += int(i[0])
    if i[1] == 'bedroom':
        b += int(i[0])
    if i[1] == 'balcony':
        cost += c*(int(i[0]) / 2)
    elif i[1] != 'balcony':
        cost += c*(int(i[0]))

print(a)
print(b)
print(cost)

