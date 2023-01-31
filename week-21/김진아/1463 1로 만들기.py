n = int(input())
arr = [0] * (1000000 + 1)
arr[1], arr[2], arr[3] = 0, 1, 1

for i in range(4, n + 1):
    if i % 3 == 0 and i % 2 == 0:
        arr[i] = min(arr[i - 1], arr[i // 3], arr[i // 2]) + 1
    elif i % 3 == 0:
        arr[i] = min(arr[i - 1], arr[i // 3]) + 1
    elif i % 2 == 0:
        arr[i] = min(arr[i - 1], arr[i // 2]) + 1
    else:
        arr[i] = arr[i - 1] + 1

print(arr[n])
