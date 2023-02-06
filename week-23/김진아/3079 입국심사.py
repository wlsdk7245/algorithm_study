n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

start, end = 0, min(arr) * m
result = 0

while start <= end:
    mid = (start + end) // 2
    people = 0
    for item in arr:
        people += mid // item

    if people >= m:
        end = mid - 1
        result = mid
    else:
        start = mid + 1

print(result)