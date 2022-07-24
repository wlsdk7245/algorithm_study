n = int(input())
graph = list(map(int, input().split()))
graph.sort()

count = 0
group = 0

for i in graph:
    group += 1
    if group >= i:
        count += 1
        group = 0

print(count)