n, m = map(int, input().split())
money = []

for _ in range(n):
    money.append(int(input()))

d = [-1] * (m+1)

maxCnt = 0

for i in money:
    for j in range(1, m + 1):
        print(i, j)
        if j % i == 0 and i <= m:
            d[j] = j // i

print(d)
