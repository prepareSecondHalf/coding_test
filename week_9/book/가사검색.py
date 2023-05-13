# 내 풀이
from bisect import bisect_left, bisect_right

def count_by_range(arr, left, right):
    rIdx = bisect_right(arr, right)
    lIdx = bisect_left(arr, left)
    
    return rIdx - lIdx

def solution(words, queries):
    answer = []
    arr = [[] for _ in range(10001)]
    
    for word in words:
        arr[len(word)].append(word)

    # 이제 뭐 어떻게 하라고
        
    return answer

# 정답
from bisect import bisect_left, bisect_right

def count_by_range(arr, left, right):
    rIdx = bisect_right(arr, right)
    lIdx = bisect_left(arr, left)
    
    return rIdx - lIdx

def solution(words, queries):
    answer = []
    arr = [[] for _ in range(10001)]
    reversed_arr = [[] for _ in range(10001)]
    
    for word in words:
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1])
        
    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()
        
    for query in queries:
        if query[0] != '?':
            res = count_by_range(arr[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
        else:
            res = count_by_range(reversed_arr[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))
            
    answer.append(res)
    return answer