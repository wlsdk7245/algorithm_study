from collections import deque

n, m = map(int, input().split())
graph = []
shark = deque()

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(m):
        if arr[j] == 1:
            shark.append((i, j))
    graph.append(arr)

dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]

def search():
    while shark:
        x, y = shark.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    shark.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1
    return

result = 0

search()
for i in range(n):
    for j in range(m):
        result = max(result, graph[i][j])

print(result - 1)