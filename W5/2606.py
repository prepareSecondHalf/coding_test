import sys
from queue import Queue

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

node = [[] for i in range(n + 1)]
vst = [False for _ in range(n + 1)]


for i in range(m):
	a, b = map(int, sys.stdin.readline().split())
	node[a].append(b)
	node[b].append(a)

def bfs(idx):
  global vst
  
  vst = [False for _ in range(n + 1)]
  que = Queue()
  vst[idx] = True
  que.put(idx)

  while not que.empty():
    curr = que.get()
    for i in node[curr]:
      if vst[i] != True:
        vst[i] = True
        que.put(i)

bfs(1)

print(vst.count(True)-1)