# import copy
#
# N, K = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# temp = copy.deepcopy(arr)
#
# S, X, Y = map(int, input().split())
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# for _ in range(S):
#     for x in range(N):
#         for y in range(N):
#             if arr[x][y] == 0:
#                 minNum = 100
#
#                 for i in range(4):
#                     nx = x + dx[i]
#                     ny = y + dy[i]
#
#                     if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 0:
#                         minNum = min(minNum, arr[nx][ny])
#
#                 if minNum != 100:
#                     temp[x][y] += minNum
#     arr = copy.deepcopy(temp)
#
# print(arr[X-1][Y-1])

from collections import deque
N, K = map(int, input().split())

graph = []
data = []

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])