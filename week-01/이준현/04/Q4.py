adventurer = int(input())
fear = list(map(int, input().split()))
count = 0
group = 0

fear.sort()

for i in fear:
    count += 1
    if count == i:
        group += 1
        count = 0
print(group)
