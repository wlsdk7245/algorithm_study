# 반례 뭔데... => 가 아니라... 방문 노드를 체크하지 않는 실수

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 1]
dy = [1, 0]
visited = [[False] * n for _ in range(n)]
result = "Hing"

def search(x, y):
    global result
    if x >= n or y >= n:
        return

    if visited[x][y]:
        return

    if graph[x][y] == -1:
        result = "HaruHaru"
        return

    visited[x][y] = True
    for i in range(2):
        nx = dx[i] * graph[x][y] + x
        ny = dy[i] * graph[x][y] + y
        search(nx, ny)

search(0, 0)

print(result)
