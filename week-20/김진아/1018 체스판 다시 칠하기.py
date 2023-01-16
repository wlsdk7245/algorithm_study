n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(input()))

check = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(x, y):
    for i in range(8):
        for j in range(8):
            for k in range(4):
                nx = dx[k] + x
                ny = dy[k] + y

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()