import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

arr = [[] for i in range(n+1)]

visitedDFS = [False] * (n + 1)
visitedBFS = [False] * (n + 1)

for _ in range(m):
    key, value = map(int, sys.stdin.readline().split())
    arr[key].append(value)
    arr[value].append(key)

for i in range(1, n+1):
    arr[i].sort()

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(arr, v, visitedDFS)
print()
bfs(arr, v, visitedBFS)

