import sys

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 1
countArr = []

def dfs(x, y):
    global count

    if x < 0 or y < 0 or x > n - 1 or y > n - 1:
        return False

    if graph[x][y] != 0:
        graph[x][y] = 0

        for i in range(4):
            if dfs(x + dx[i], y + dy[i]) == True:
                count += 1
        return True
    return False


result = 0

for i in range(n):
    for j in range(n):

        if dfs(j, i) == True:
            countArr.append(count)
            count = 1
            result += 1

countArr.sort()

print(result)
for i in countArr:
    print(i)