# 브론즈 3. 바이러스
# 사실상 내 코드가 아님...

from collections import deque

N = int(input())
M = int(input())

graph = [[]*N for i in range(N+1)]
visited = [0] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    q = deque([x])
    visited[x] = True
    c = 0

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                q.append(nx)
                visited[nx] = True
                c += 1
    return c

# 1번 컴퓨터를 통해 걸리는 바이러스
print(bfs(1))