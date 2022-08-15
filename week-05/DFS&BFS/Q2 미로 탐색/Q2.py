import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1:
                continue
            if graph[nx][ny] == 0:
                continue
            elif graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(search(0, 0))

