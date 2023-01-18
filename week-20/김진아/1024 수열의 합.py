n, l = map(int, input().split())
length = l
check = False

while True:
    result = 0
    x = (n - sum(range(length))) // length
    if x < 0:
        break

    for i in range(length):
        result += x + i

    if result == n:
        check = True
        for i in range(length):
            print(x + i, end=' ')
        break
    else:
        length += 1

    if length > 100:
        break

if not check:
    print(-1)