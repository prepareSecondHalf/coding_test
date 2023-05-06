from sys import stdin
_ = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
_ = stdin.readline()
M = map(int,stdin.readline().split())

def binary(n, N, start, end):
    if start > end: # start가 end보다 커지면 0을 리턴
        return 0
    m = (start+end)//2
    if n == N[m]: #중간값이 n과 같으면
        return N[start:end+1].count(n) # N에서 start~end값까지 제외후 갯수 return
    elif n < N[m]: # 중간값이 n보다 크면 end값을 줄임
        return binary(n, N, start, m-1)
    else: # 중간값이 n보다 작으면 start값을 늘림
        return binary(n, N, m+1, end)

n_dic = {}
for n in N:
    start = 0
    end = len(N) - 1
    if n not in n_dic:
        n_dic[n] = binary(n, N, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M ))
