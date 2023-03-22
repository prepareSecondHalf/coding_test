# 데이터 처리 전문가가 되고 싶은 "어피치"는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다.
# 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데, 
# 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.
# 간단한 예로 "aabbaccc"의 경우 "2a2ba3c"(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데, 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 
# 예를 들면, "abcabcdede"와 같은 문자열은 전혀 압축되지 않습니다. 
# "어피치"는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.
# 예를 들어, "ababcdcdababcdcd"의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 "2ab2cd2ab2cd"로 표현할 수 있습니다. 
# 다른 방법으로 8개 단위로 잘라서 압축한다면 "2ababcdcd"로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.
# 다른 예로, "abcabcdede"와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 "abcabc2de"가 되지만, 3개 단위로 자른다면 "2abcdede"가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다. 
# 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.
# 압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.

# s의 길이는 1~1000이며 소문자로만 이루어져 있다.

# 문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.
# 따라서 주어진 문자열("xababcdcdababcdcd")을 x / ababcdcd / ababcdcd 로 자르는 것은 불가능 합니다.
# 이 경우 어떻게 문자열을 잘라도 압축되지 않으므로 가장 짧은 길이는 17이 됩니다.


def solution(s):
    answer = 0
    # 풀이: 1 ~ s-1개 단위로 완전 탐색을 해도 최대 1000개이므로 상관없어 보인다. 이중으로 해도 1000000이므로 여유로움(아마)
    min_length = 1000
    # 단위가 전체 길이의 절반이 넘어가면 압축이 되지 않으므로 단위는 최대 '전체 길이 // 2'
    units = list(range(1, len(s)//2+1))
    print('units', units)
    for unit in units:
        repeated = s[:unit]
        print('repeated', repeated)
        compressed_time = 0
        compressed_s = ''
        idx = 0
        while True:
            if (idx+1)*unit-1 >= len(s):
                print('compressed_s', compressed_s)
                break

            compared = s[idx*unit:(idx+1)*unit-1]
            print('compared', compared)
            if repeated == compared:
                compressed_time += 1
            else:
                if compressed_time > 1:
                    compressed_s += str(compressed_time) + repeated
                else:
                    compressed_s += compared
                compressed_time = 0
            idx += 1





    return answer

solution('abababababaaaaa')