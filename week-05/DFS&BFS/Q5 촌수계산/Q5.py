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
    for i in arr[x]:
        if visited[i] == 0:
            visited[i] = visited[v] + 1
            search(v)

            if i == b:
                break

search(a)

if visited[b] > 0:
    print(visited[b])
else:
    print(-1)

# def search(graph, v, visited):
#     global count, index, isFind
#
#     if v == b:
#         count = index
#         isFind = True
#
#     index += 1
#     visited[v] = True
#
#     for i in graph[v]:
#         if not visited[i]:
#             search(graph, i, visited)
#
# search(arr, a, visited)
#
# if isFind == True:
#     print(count)
# else:
#     print(-1)
