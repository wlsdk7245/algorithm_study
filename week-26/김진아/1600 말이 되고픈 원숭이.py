k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
visited = [[False] * w for _ in range(h)]
mx = [0, 0, -1, 1]
my = [-1, 1, 0, 0]

hx = [-2, -1, -2, -1, 1, 2, 1, 2]
hy = [-1, -2, 1, 2, -2, -1, 2, 1]
find = False

answer = []
def search(x, y, count, result):
    print(x, y)
    visited[x][y] = True
    if x == w - 1 and y == h - 1:
        print('x, y', x, y)
        answer.append(result)
        return



    if count > 0:
        for i in range(8):
            nhx, nhy = x + hx[i], y + hy[i]
            if 0 <= nhx < w and 0 <= nhy < h:
                if arr[nhx][nhy] != 1 and not visited[nhx][nhy]:
                    print('nhx, nhy', nhx, nhy, result + 1)
                    search(nhx, nhy, count - 1, result + 1)

    for i in range(4):
        nmx, nmy = x + mx[i], y + my[i]

        if 0 <= nmx < w and 0 <= nmy < h:
            if arr[nmx][nmy] != 1 and not visited[nmx][nmy]:
                print('nmx, nmy', nmx, nmy, result + 1)
                search(nmx, nmy, count, result + 1)



search(0, 0, k, 0)

print(answer)