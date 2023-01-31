import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
start, end = 1, max(arr)

while start <= end:
    # 중간값 구하기
    mid = (start + end) // 2
    count = 0

    for item in arr:
        count += item // mid
    if count >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)