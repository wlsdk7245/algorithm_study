n = int(input())

station = []

for _ in range(n):
    a, b = map(int, input().split())
    station.append([a, b])

l, p = map(int, input().split())

current = 0
currentOil = 0

result = 0

for a, b in station:
    if p >= a - current:
        p -= a - current
    else:
        if current == 0:
            result = -1
            break
        else:
            p += currentOil
            result += 1

            if p >= a - current:
                p -= a - current
            else:
                result = -1
                break

    current = a
    currentOil = b

if p >= l - current:
    p -= l - current
else:
    p += currentOil
    result += 1
    if p >= l - current:
        p -= l - current
    else:
        result = -1

print(result)