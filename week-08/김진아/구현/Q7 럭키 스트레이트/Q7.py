n = input()

midIndex = int(len(n) / 2)

leftSum = 0
rightSum = 0

for i in range(len(n)):
    if i < midIndex:
        leftSum += int(n[i])
    else:
        rightSum += int(n[i])

if leftSum == rightSum:
    print('LUCKY')
else:
    print('READY')