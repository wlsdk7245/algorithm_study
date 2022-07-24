# Part 3 - Chapter 06 정렬 1 - 국영수
n = int(input())
score = [input().split() for _ in range(n)]

result = sorted(score, key=lambda data: (-int(data[1]), int(data[2]), -int(data[3]), data[0]))

for i in result:
    print(i[0])