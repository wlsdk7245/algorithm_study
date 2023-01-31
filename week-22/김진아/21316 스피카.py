arr = [[] for _ in range(13)]

for i in range(12):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, 13):
    if len(arr[i]) == 3:
        temp = []
        for item in arr[i]:
            temp.append(len(arr[item]))
        if max(temp) == 3 and sum(temp) == 6 and min(temp) == 1:
            break

print(i)