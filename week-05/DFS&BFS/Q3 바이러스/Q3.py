import sys

n = int(input())
p = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(p):
    key, value = map(int, sys.stdin.readline().split())
    graph[key].append(value)
    graph[value].append(key)

for i in range(1, n + 1):
    graph[i].sort()

count = 0

def search(graph, v, visited):
    visited[v] = True
    global count
    if v != 1:
        count += 1
    for i in graph[v]:
        if not visited[i]:
            search(graph, i, visited)

search(graph, 1, visited)

print(count)