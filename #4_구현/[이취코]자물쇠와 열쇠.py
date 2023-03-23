def solution(key, lock):
    answer = True
    '''
    lock의 홈 부분 모양이 key 모양과 일치 여부 파악
    영역을 벗어난 부분은 상관 없음
    일치 여부 파악을 위해 key 모양을 시계방향으로(임의 기준) 회전시키며 모양이 맞는지 파악
        
    before
    [
        [(0,0), (0, 1), (0,2)]
        [(1,0), (1, 1), (1,2)]
        [(2,0), (2, 1), (2,2)]
    ]
    
    after(시계방향 90도 회전)
    [
        [(2,0), (1, 0), (0,0)]
        [(2,1), (1, 1), (0,1)]
        [(2,2), (1, 2), (0,2)]
        
        [(i + 2, 0), (i + 1, i - 1), (0, i + 2)]
        [(i - 1, i - 1), (i, i), (i + 1, 1 + 1)]
        [(i, i - 2), (i - 1, i + 1), (i + 2 , i)]
    ]
    
    after(시계방향 180도 회전)
    [
        [(2,2), (2, 1), (2,0)]
        [(1,2), (1, 1), (1,0)]
        [(0,2), (0, 1), (0,0)]
    ]
        
    after(시계방향 270도 회전)
    [
        [(0,2), (1,2), (2,2)]
        [(0,1), (1,1), (2,1)]
        [(0,0), (1,0), (2,0)]
    ]
    
    after(시계방향 360도 회전)
    : 첫 모양과 동일
    
    key = 
    before:
    [
        [0, 0, 0], 
        [1, 0, 0], 
        [0, 1, 1]
    ]	
    
    after:
    [
        [0, 1, 0], 
        [1, 0, 0], 
        [1, 0, 0]
    ]	
    
    lock = 
    [
        [1, 1, 1], 
        [1, 1, 0], 
        [1, 0, 1]
    ]	
    
    '''
    
    
    
    return answer


''' 답안 예시'''
# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock)
    
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    

    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        
        for x in range(n * 2):
            for y in range(n * 2):

                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                if check(new_lock) == True:
                    return True
            
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
                        
    return False