import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    s = 0
    pre = 0

    length = len(food_times)

    while s + ((q[0][0] - pre) * length) <= k:
        now = heapq.heappop(q)[0]
        s += (now - pre) * length
        length -= 1
        pre = now 
    result = sorted(q, key=lambda x: x[1])
    return result[(k - s) % length][1]