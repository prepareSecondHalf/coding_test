count = int(input())

list = []
for i in range(count):
    w, h = map(int, input().split())
    list.append([w, h])

for i in list : #0
    rank = 1 #1 
    
    for j in list:
        if (i[0] != j[0]) & (i[1] != j[1]):
            if (i[0 ]< j[0]) & (i[1 ]< j[1]):
                rank += 1
            
    print(rank)