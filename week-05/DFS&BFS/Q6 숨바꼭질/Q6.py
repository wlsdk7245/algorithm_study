import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())

maximum = 2 * 100000 + 1
visited = [0] * maximum

def search(v):
    queue = deque([v])

    while queue:
        v = queue.popleft()
        if v == k:
            return visited[k]

        for i in (v - 1, v + 1, v * 2):
            if 0 <= i < maximum and not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)

            # if i < 0 or i > maximum:
            #     continue
            # elif visited[i] != 0:
            #     continue
            # else:
            #     visited[i] = visited[v] + 1
            #     queue.append(i)

print(search(n))
