import sys
a = sys.stdin.readline().strip()
b = a.split('-')
number_list = []
result = 0
for i in range(len(b)):
    x = b[i].split('+')
    count = 0
    for j in range(len(x)):
        count += int(x[j])
    number_list.append(count)

# print(number_list)
for k in range(1, len(number_list)):
    result -= number_list[k]

result = int(number_list[0]) + result
print(result)