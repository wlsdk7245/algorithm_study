n = int(input())
p = list(map(int, input().split()))
p.sort()

arr = []
result = 0

for i in p:
    result += i
    arr.append(result)

print(sum(arr))