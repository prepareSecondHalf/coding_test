# x = input("5 8 3\n2 4 5 4 6")
# n = int(input())
# conditions = list(map(int, input()))
# nums = list(map(int, input()))

conditions = [5, 8, 3]
nums = [2, 4, 5, 4, 6]
n = conditions[0] # 크기
m = conditions[1] # 더하기 횟수
k = conditions[2] # 연속 더하기 횟수


max = 0
maxArr = []
cnt = 0
for idx in range(m) :
    for t in nums:
        if (maxArr[idx] and t > max) :
            max = t
            maxArr.append(max)
        elif (maxArr[idx] < t and t > max ): 
            max = t
            maxArr.append(max)
    
print(t, max, maxArr)



