from collections import deque

n, m, k, x = map(int, input().split())
arr = [[] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

distance = [-1] * (n + 1)
distance[x] = 0
q = deque([x])

while q:
    cur = q.popleft()

    for i in arr[cur]:
        if distance[i] == -1:
            distance[i] = distance[cur] + 1
            q.append(i)

check = False

for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)