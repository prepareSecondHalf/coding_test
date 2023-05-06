# 백준: 1715
# n: 숫자카드 묶음의 수
# 각 카드묶음의 장수
# 출력: 최소 비교횟수
import sys, heapq

n = int(sys.stdin.readline())
card = []
for _ in range(n):
    card.append(int(sys.stdin.readline()))

heapq.heapify(card) #정렬
cnt = 0

while len(card) > 1:
    # 가장작은 카드와 그다음 작은 카드의 수를 card에서 적출 및 정렬후 더해서 다시 삽입후 cnt에 그값을 더해줌
    tmp = heapq.heappop(card) + heapq.heappop(card)
    heapq.heappush(card, tmp)
    cnt += tmp

print(cnt)

# heappop(heap): 가장작은 원소를 빼고 나머지 원소가 힙을 유지하도록 정렬
# heappush(heap, data) : heap 상태를 유지하며 data를 삽입
# heapify : 주어진 리스트를 힙정렬

