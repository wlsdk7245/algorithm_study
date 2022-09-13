n = int(input())
arr = list(map(int, input().split()))
arr.sort()

group = 0
cnt = 0

for i in arr:
    group += 1
    if group >= i:
        cnt += 1
        group = 0

print(cnt)