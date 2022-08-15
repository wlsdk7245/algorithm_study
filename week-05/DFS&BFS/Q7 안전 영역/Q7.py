from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

maximum = 0

for i in range(n):
    maximum = max(max(graph[i]), maximum)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(x, y, node):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > node and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

result = 0

for i in range(1, maximum + 1):
    visited = [[False] * n for _ in range(n)]
    count = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and not visited[j][k]:
                visited[j][k] = 1
                search(j, k, i)
                count += 1

    if result < count:
        result = count

if result > 0:
    print(result)
else:
    print(1)