n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]
A.reverse()

count = 0

while k:
    for coin in A:
        count += k // coin
        k %= coin

print(count)