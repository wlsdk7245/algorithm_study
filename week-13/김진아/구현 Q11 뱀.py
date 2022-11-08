from collections import deque

N = int(input())
K = int(input())
apple = [[0] * N for _ in range(N)]

for _ in range(K):
    x, y = map(int, input().split())
    apple[x - 1][y - 1] = 1

L = int(input())

snakeDirection = {}
for _ in range(L):
    X, C = input().split()
    snakeDirection[int(X)] = C

snake = deque([[0, 0]])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

d = 1
time = 0
nx, ny = 0, 0

while True:
    time += 1
    nx += dx[d]
    ny += dy[d]

    if time in snakeDirection.keys():
        if snakeDirection[time] == "D":
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4

    if 0 <= nx < N and 0 <= ny < N:
        if [nx, ny] in snake:
            break

        if apple[nx][ny] == 1:
            apple[nx][ny] = 0
            snake.append([nx, ny])

        else:
            snake.append([nx, ny])
            x, y = snake.popleft()
    else:
        break

print(time)
