n = list(map(int, input()))

length = len(n) // 2
left = sum(n[0:length])
right = sum(n[length:])

if left == right:
    print('LUCKY')

else:
    print('READY')