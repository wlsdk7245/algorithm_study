N = int(input())
dataSet = list(map(int, input().split()))
dataSet.sort()

group = 0
cnt = 0

for i in dataSet:
    group += 1
    if group >= i:
        cnt += 1
        group = 0

print(cnt)

