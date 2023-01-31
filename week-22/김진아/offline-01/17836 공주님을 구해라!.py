from collections import deque
n, m, t = map(int, input().split())
princess = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
q.append((0, 0, 0))

visited = [[False] * m for _ in range(n)]

visited[0][0] = True
result = 1e9

while q:
    x, y, d = q.popleft()

    if x == n - 1 and y == m - 1:
        result = min(result, d)
        break

    if d + 1 > t:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if princess[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny, d + 1))
            elif princess[nx][ny] == 1:
                continue
            elif princess[nx][ny] == 2:
                temp = d + 1
                temp += (n - 1 - nx) + (m - 1 - ny)
                visited[nx][ny] = True
                if temp <= t:
                    result = temp

if result > t:
    print('Fail')
else:
    print(result)