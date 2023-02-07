# from collections import deque
#
# n, k = map(int, input().split())
# graph = [-1] * 100001
# graph[n] = 0
# queue = deque([n])
#
# while queue:
#     target = queue.popleft()
#
#     if target == k:
#         print(graph[target])
#         exit(0)
#
#     for i in (target + 1, target - 1, target * 2):
#         if 0 <= i <= 100000 and graph[i] == -1:
#             if i == target * 2:
#                 graph[i] = graph[target]
#                 queue.appendleft(i)
#             else:
#                 graph[i] = graph[target] + 1
#                 queue.append(i)
#

from collections import deque
n, k = map(int, input().split())
graph = [-1] * 100001

q = deque([n])
graph[n] = 0

while q:
    now = q.popleft()

    if now == k:
        break

    if 0 <= now - 1 < 100001 and graph[now - 1] == -1:
        graph[now - 1] = graph[now] + 1
        q.append(now - 1)
    if 0 < now * 2 < 100001 and graph[now * 2] == -1:
        graph[now * 2] = graph[now]
        q.appendleft(now * 2)
    if 0 <= now + 1 < 100001 and graph[now + 1] == -1:
        graph[now + 1] = graph[now] + 1
        q.append(now + 1)
print(graph[k])