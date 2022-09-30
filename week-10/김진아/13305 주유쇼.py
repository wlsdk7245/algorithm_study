n = int(input())

road = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
cost = price[0]

for i in range(len(road)):
    cost = min(cost, price[i])
    result += road[i] * cost

print(result)
