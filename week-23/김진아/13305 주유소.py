# n = int(input())
# road = list(map(int, input().split()))
# city = list(map(int, input().split()))
#
# d = [0] * n
#
# d[1] = city[0] * road[0]
#
# for i in range(2, n):
#     temp = city[0:i]
#     d[i] = road[i - 1] * min(temp) + d[i - 1]
#
# print(d[n - 1])

n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))

result = 0
cost = city[0]

for i in range(len(road)):
     cost = min(cost, city[i])
     result += road[i] * cost

print(result)