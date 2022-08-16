n, m, c = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x][y] = z

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

timeArr = []

for a in range(1, n + 1):
    if graph[c][a] != INF and graph[c][a] != 0:
        timeArr.append(graph[c][a])

timeArr.sort()

for a in timeArr:
    print(a, end=" ")
