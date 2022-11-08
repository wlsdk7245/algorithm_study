N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0
groupCount = 0

for i in arr:
    groupCount += 1
    if groupCount >= i:
        result += 1
        groupCount = 0

print(result)