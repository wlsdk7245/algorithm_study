import sys
input = sys.stdin.readline

a = {"R": (1, 0), "L": (-1, 0), "B": (0, -1), "T": (0, 1), "RT": (1, 1), "LT": (-1, 1), "RB": (1, -1), "LB": (-1, -1)}

k, s, N = input().split()
N = int(N)

kx, ky = k
kx = ord(kx) - 64
ky = int(ky)

sx, sy = s
sx = ord(sx) - 64
sy = int(sy)

directions = []
for _ in range(N):
    directions.append(a[input().rstrip()])

for d in directions:
    nkx = kx + d[0]
    nky = ky + d[1]
    # 움직일 킹의 자리가 범위 내임
    if 1 <= nkx <= 8 and 1 <= nky <= 8:
        # 킹이 가야하는 자리에 돌이 있는 경우
        if nkx == sx and nky == sy:
            nsx = sx + d[0]
            nsy = sy + d[1]

            # 움직일 돌의 자리가 범위 내임
            if 1 <= nsx <= 8 and 1 <= nsy <= 8:
                kx, ky = sx, sy
                sx, sy = nsx, nsy
            # 움직일 돌의 자리가 범위 바깥임
            else:
                continue
        # 킹이 가야하는 자리에 돌이 없는 경우
        else:
            kx, ky = nkx, nky
    # 움직일 킹의 자리가 범위 바깥임
    else:
        continue

print(chr(kx + 64) + str(ky))
print(chr(sx + 64) + str(sy))
