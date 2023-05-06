# n
# n개의 정수
# m
# m개의 정수
# m개의 정수들이 n개의 정수들에 포함되어있는지 확인

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

for i in b:
    if i in a:
        print(1)
    else:
        print(0)

#질문 set대신 list를 사용하면 시간초과가 뜸 set이랑 list랑 왜 속도에서 차이가 나는건지?