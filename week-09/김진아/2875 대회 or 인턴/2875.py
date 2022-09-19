n, m, k = map(int, input().split())

sumCnt = n + m
minCnt = min(n // 2, m)
result = minCnt
remains = sumCnt - (minCnt * 3)

while True:
    remains = sumCnt - (minCnt * 3)
    if remains - k < 0:
        result -= 1
        k -= 3
    else:
        break
    if k <= 0:
        break

print(result)