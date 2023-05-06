# n: 학생수
# 학생이름, 국영수 점수
# 출력 국어점수가 감소하는순서 -> 영어점수가 증가하는순서 -> 수학점수가 감소하는순서 -> 이름이 사전순으로 증가하는 순서
n = int(input())
student = []
for _ in range(n):
    student.append(list(map(str,input().split())))
student.sort(key=lambda x : str(x[0])) # 이름순으로 정렬
student.sort(key=lambda x:int(x[3]), reverse=True) # 수학점수가 감소하는순으로 정렬
student.sort(key = lambda x : int(x[2])) # 영어점수 증가하는순으로 정렬
student.sort(key = lambda x: int(x[1]), reverse = True) # 국어점수가 감소하는순으로 정렬

for i in student:
    print(i[0])