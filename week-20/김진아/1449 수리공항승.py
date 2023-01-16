n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

if l == 1:
    print(n)

else:
    length = l
    count = 1

    prev = arr[0]

    for i in range(1, n):
        if arr[i] - prev <= length:
            length -= 1
        else:
            count += 1
            length = l

        if length == 0:
            length = l
            count += 1
        prev = arr[i]

    print(count)