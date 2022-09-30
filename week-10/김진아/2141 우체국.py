n = int(input())

post = list(list(map(int, input().split())) for _ in range(n))
post.sort()

people = 0

for i in range(n):
    people = people + post[i][1]

mid = people // 2

if people % 2 != 0:
    mid += 1

count = 0

for a, b in post:
    count += b
    if count >= mid:
        result = a
        break

print(result)