n = int(input())
arr = []

INF = 1e9
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    arr.append((a, b))
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


result = []
for i in range(1, n + 1):
    result.append(max(graph[i][1:]))

print(min(result), result.count(min(result)))
for i in range(n):
    if result[i] == min(result):
        print(i + 1, end=' ')
