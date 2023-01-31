n, m = map(int, input().split())

arr = [int(input()) for _ in range(n)]
start, end = min(arr), sum(arr)

while start <= end:
    mid = (start + end) // 2
    bank = mid
    count = 1

    for today in arr:
        if bank < today:
            bank = mid
            count += 1
        bank -= today

    if count > m or mid < max(arr):
        start = mid + 1
    else:
        end = mid - 1
        k = mid

print(k)