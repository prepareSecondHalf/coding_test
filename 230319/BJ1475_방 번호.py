# 다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.
# 다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오. (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)

# 첫째 줄에 다솜이의 방 번호 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수이다.

# 첫째 줄에 필요한 세트의 개수를 출력한다.

import sys
import math

n = int(sys.stdin.readline().strip())

# 방 번호에 있는 9를 6으로 변환 후 정렬
# 각 원소의 개수를 셈(6은 2로 나눈 몫 올림)
# 가장 큰 원소의 개수가 세트 수
converted_n = sorted(str(n).replace('9', '6'))
# print(converted_n)
needed_set = 0
# 9는 6으로 바꿨으니 0~8만 검사하면 됨. 숫자가 작을 때는 비효율적이지만 커질수록 반복량이 줄어서 좋을 듯?
for number in range(9):
    if (number == 6):
        needed_number = math.ceil(converted_n.count(str(number))/2)
    else:
        needed_number = converted_n.count(str(number))

    if needed_set < needed_number:
        needed_set = needed_number
print(needed_set)