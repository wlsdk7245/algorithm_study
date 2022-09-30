n = int(input())

arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x:(x[1], x[0]))

result = 0
end = 0

for i, j in arr:
    if i >= end:
        result += 1
        end = j

print(result)

# 정답은 맞았는데 메모리 무슨 일?
