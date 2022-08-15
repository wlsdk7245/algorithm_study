# 브론즈 2. DFS와 BFS
# 그나마 기본문제였긴함...

N, M, V = map(int, input().split())

s = [[0] * (N + 1) for i in range(N + 1)]

# 방문 리스트
visit = [0 for i in range(N + 1)]
for i in range(M):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1

# DFS
def dfs(V):
    print(V, end=' ')
    visit[V] = 1
    for i in range(1, N + 1):
        if visit[i] == 0 and s[V][i] == 1:
            dfs(i)

# BFS
def bfs(V):
    queue = [V]
    visit[V] = 0
    while (queue):
        V = queue[0]
        print(V, end=' ')
        del queue[0]
        for i in range(1, N + 1):
            if visit[i] == 1 and s[V][i] == 1:
                queue.append(i)
                visit[i] = 0

dfs(V)
print()
bfs(V)