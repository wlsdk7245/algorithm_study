N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
max_value = 0
count = 0

arr.sort(reverse=True)
MAX = arr[0]
SECOND_MAX = arr[1]

for _ in range(M):
    if count < K:
        max_value += MAX
        count += 1
    else:
        max_value += SECOND_MAX
        count = 0

print(max_value)
