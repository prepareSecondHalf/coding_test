import sys
import heapq as HQ
input = sys.stdin.readline

# 입력받은 각 카드 묶음의 개수를 힙에 삽입
Deck = []
for _ in range(int(input())):
  HQ.heappush(Deck, int(input()))

result = 0
# 작은 값부터 꺼내면서 계산
while len(Deck) > 1:
  # heappop은 불변성 유지하면서 가장 작은 항목을 팝하고 반환
  tmp = HQ.heappop(Deck) + HQ.heappop(Deck)
  result += tmp
  HQ.heappush(Deck, tmp)
print(result)