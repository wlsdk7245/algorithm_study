n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def search(x, y):
    global answer
    answer += 2

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 옆이 비어있지 않은 경우
        if 0 <= nx < n and 0 <= ny < m:
            # 옆에 있는 거 보다 높이 올라온 경우
            if arr[x][y] > arr[nx][ny]:
                answer += arr[x][y] - arr[nx][ny]

        # 옆이 비어있는 경우
        else:
            answer += arr[x][y]

for i in range(n):
    for j in range(m):
        search(i, j)

print(answer)