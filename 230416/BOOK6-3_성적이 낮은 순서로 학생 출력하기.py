# N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 성적으로 구분된다.
# 각 학생의 이름과 성적이 주어졌을 때, 성적이 낮은 순서대로 학생의 이름을 출력하시오

# 입력
# 첫 번째 줄에 학생의 수 N이 입력된다. (1 <= N <= 100000)
# 두 번째 줄부터 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다.
# 문자열 A의 길이와 학생의 성적은 100 이하의 자연수이다.

# 출력
# 모든 학생의 이름을 성적이 낮은 순서대로 출력한다. 
# 성적이 동일한 학생들의 순서는 자유롭게 출력해도 된다.

# 풀이
# 딕셔너리를 사용하고 특정 key를 기준으로 정렬하면 된다

import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    a, b = sys.stdin.readline().split()
    data.append({ "name": a, "score": int(b) })

data.sort(key=lambda x: x["score"])
for item in data:
    print(item["name"])