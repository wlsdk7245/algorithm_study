def func():
    n = int(input())
    road = []

    road.append(sum(list(map(int, input().split()))))

    for i in range(n):
        road.append(sum(list(map(int, input().split()))))

    road.append(sum(list(map(int, input().split()))))

    for i in range(1, n + 2):
        if road[i] - road[i - 1] > 1000:
            return 'sad'

    return 'happy'

t = int(input())
for _ in range(t):
    result = func()
    print(result)