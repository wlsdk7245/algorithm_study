N, K = map(int, input().split())

cnt = 0

while True:
    if N % K == 0:
        N = N / K
    else:
        N = N - 1
    cnt += 1
    if N == 1:
        break

print(cnt)
