import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

time = int(1e9)
height = 0

for i in range(257):
    plus = 0
    minus = 0

    for x in range(N):
        for y in range(M):
            if arr[x][y] > i:
                plus += arr[x][y] - i
            else:
                minus += i - arr[x][y]

    if minus > plus + B:
        continue

    count = plus * 2 + minus

    if count <= time:
        time = count
        height = i

print(time, height)