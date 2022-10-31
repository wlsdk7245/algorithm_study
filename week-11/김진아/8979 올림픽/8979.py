n, k = map(int, input().split())
nations = []
medals = []

for i in range(n):
    a, b, c, d = map(int, input().split())
    nations.append([a,b, c, d])

nations.sort(key=lambda x:(-x[1], -x[2], -x[3]))

index = 0

for i in range(len(nations)):
    if k == nations[i][0]:
        index = i


while True:
    if index == 0:
        break
    else:
        if nations[index][1:] == nations[index-1][1:]:
            index -= 1
            continue
        else:
            break

print(index + 1)