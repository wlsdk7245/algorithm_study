import sys
sys.setrecursionlimit(300000)

n = int(input())
a, b = map(int, input().split())
m = int(input())

arr = [[] for i in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

def search(v):
    for i in arr[v]:
        if visited[i] == 0:
            visited[i] = visited[v] + 1
            search(i)

search(a)

if visited[b] > 0:
    print(visited[b])
else:
    print(-1)
