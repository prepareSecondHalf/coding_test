import sys

N = int(sys.stdin.readline())

students = []

for _ in range(N):
	name, kor, en, math = sys.stdin.readline().strip().split()
	students.append((name, int(kor), int(en), int(math)))

students = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
	print(student[0])