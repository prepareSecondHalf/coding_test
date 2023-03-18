import sys

n = int(sys.stdin.readline())
time = [0, 0, 0]
count = 0

while time[0] < n+1:
    time[2] += 1
    if time[2] == 60:
        time[1] += 1
        time[2] = 0

    if time[1] == 60:
        time[0] += 1
        time[1] = 0

    if '3' in str(time[0]) or '3' in str(time[1]) or '3' in str(time[2]):
        count += 1
        print(time)

print(count)