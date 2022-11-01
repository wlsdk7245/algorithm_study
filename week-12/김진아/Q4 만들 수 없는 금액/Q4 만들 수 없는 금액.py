N = int(input())
arr = list(map(int, input().split()))
arr.sort()

minNum = 1

for i in arr:
    if minNum < i:
        break
    minNum += i

print(minNum)
