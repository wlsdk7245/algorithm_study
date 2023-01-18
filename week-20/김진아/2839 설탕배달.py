n = int(input())

result = 10001

for i in range(0, n // 3 + 1):
    num = n - (i * 3)
    if num % 5 == 0:
        result = min(i + num // 5, result)

if result == 10001:
    print(-1)
else:
    print(result)