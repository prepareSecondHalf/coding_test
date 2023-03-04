numList = list(input().split())
sum = int(0)

for i in range(len(numList)):
    sum += (int(numList[i]) ** 2)
    
print(divmod(sum, 10)[1])