# 당신은 부동산 회사의 소프트웨어 개발자 중 한 명입니다. 
# 구현할 기능 중 하나는 대리점이 판매하는 아파트에 대해 다른 유형의 통계를 계산하는 것입니다. 
# 각 아파트는 침실, 욕실, 부엌, 발코니 등 다양한 유형의 방으로 구성되어 있습니다.
# 이 아파트의 비용은 총면적 감소와 1평방미터 비용의 곱과 같습니다. 
# 줄어든 총 면적은 발코니를 제외한 모든 객실의 총 면적에 발코니 전체 면적의 절반을 더한 것입니다.

# 아파트의 각 객실 면적과 1평방미터의 비용에 대한 정보가 제공됩니다. 플랫에 대해 다음 값을 계산해야 합니다:

# 모든 객실의 총 면적;
# 모든 침실의 총 면적;
# 아파트의 가격.


# 입력 파일의 첫 번째 줄에는 두 개의 정수 n(1 ≤ n ≤ 10)과 c(1 ≤ c ≤ 100 000)가 포함됩니다. 
# 즉, 플랫에 있는 방의 수와 1 평방 미터의 비용입니다.
# 다음의 각 n행은 각각 정수 ai(1 ≤ ai ≤ 100)와 단어 ti(i-throom의 면적 및 유형)를 포함합니다. 
# 단어 ti는 "침대", "화장실", "주방", "발코니", "기타" 중 하나입니다.

# 출력 파일의 첫 번째 줄에는 하나의 정수(평면의 모든 룸의 총 면적)가 포함되어야 합니다. 
# 출력 파일의 두 번째 줄에는 하나의 정수, 즉 플랫의 총 침실 면적이 포함되어야 합니다. 
# 출력 파일의 세 번째 줄에는 하나의 실수가 포함되어야 합니다. 즉, 정밀도가 10^-6 이하인 플랫의 비용입니다.

import sys
n, c = map(int, sys.stdin.readline().split()) # n: 방의 수, c: 평당 가격

rooms = []
for i in range(n):
    area, type = map(str, sys.stdin.readline().split()) # 평수, 방 종류
    rooms.append({ "area": int(area), "type": type })

total_area = 0
bedroom_area = 0
total_cost = 0
for room in rooms:
    total_area += room["area"]
    
    if room["type"] == "bedroom":
        bedroom_area += room["area"]
    
    if room["type"] == "balcony":
        total_cost += room["area"] * c / 2
    else:
        total_cost += room["area"] * c

print(total_area)
print(bedroom_area)
print(total_cost)