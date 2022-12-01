N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
temp = [[0] * M for _ in range(M)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < N and ny>=0 and ny < M:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result

    if count == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = graph[i][j]

        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, get_score())
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1

dfs(0)
print(result)

# 벽을 3개 세워야하는 것은 필수 => 벽 세웠을 때 바이러스 퍼뜨려야함
# 단절점 찾기 dfs
# 바이러스 퍼뜨린 후 빈칸 몇개인지 체크하고 최대값 찾음

