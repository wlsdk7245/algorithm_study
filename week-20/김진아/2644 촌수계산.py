from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

visited = [False] * (n + 1)
count = [0] * (n + 1)

queue = deque()
queue.append(a)

while queue:
    temp = queue.popleft()
    visited[temp] = True

    for i in arr[temp]:
        if not visited[i]:
            queue.append(i)
            count[i] = count[temp] + 1
        else:
            continue

if count[b] != 0:
    print(count[b])
else:
    print(-1)