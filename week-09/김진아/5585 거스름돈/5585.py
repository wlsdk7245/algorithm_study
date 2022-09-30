m = int(input())

changes = 1000 - m
count = 0

while changes:
    if changes >= 500:
        count += changes // 500
        changes %= 500
        continue
    if changes >= 100:
        count += changes // 100
        changes %= 100
        continue
    if changes >= 50:
        count += changes // 50
        changes %= 50
        continue
    if changes >= 10:
        count += changes // 10
        changes %= 10
        continue
    if changes >= 5:
        count += changes // 5
        changes %= 5
        continue
    if changes >= 1:
        count += changes // 1
        changes %= 1
        continue

print(count)
