# 실버1. 단지번호붙이기
# 단지 수 세는거만 생각하고 있었는데 그 안에 집 수도 세라길래 너무 화가 났다...
# 물론 다른 사람 풀이 봤지만 그래도 이건 bfs dfs 분류인거 정도는 알 수 있을듯?

from collections import deque

N = int(input())

graph = [list(map(int, input())) for _ in range(N)]

def bfs(graph, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt

count = [bfs(graph, i, j) for i in range(N) for j in range(N) if graph[i][j] == 1]

count.sort()
print(len(count))

for i in range(len(count)):
    print(count[i])