# 실버1. 숨바꼭질
# 전혀 모르겠는데 답 보니까 코드는 짧아서 약올라
# not 구문 처음보는거같은데 진짠가

from collections import deque

N, K = map(int, input().split())
max = 100000
visited = [0] * (max+1)

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(visited[x])
            break
        for j in (x-1, x+1, x*2):
            if 0<= j <= max and not visited[j]:
                visited[j] = visited[x] + 1
                q.append(j)

bfs()