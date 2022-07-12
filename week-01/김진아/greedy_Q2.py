N, M = map(int, input().split())

result = 0

for i in range(N):
    dataSet = list(map(int, input().split()))
    result = max(result, min(dataSet))

print(result)


