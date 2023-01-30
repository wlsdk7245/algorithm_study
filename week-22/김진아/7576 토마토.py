from collections import deque
m, n = map(int, input().split())
tomato = []

q = deque()

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 1:
            q.append((i, j))
    tomato.append(temp)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                q.append((nx, ny))

solution()

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit(0)

result = max(map(max, tomato))
print(result - 1)