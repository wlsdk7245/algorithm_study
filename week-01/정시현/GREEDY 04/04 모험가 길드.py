# GREEDY 04.모험가 길드

n = map(int, input())

fear = list(map(int, input().split()))
fear.sort()

count = 0

max_fear = max(fear)

while max_fear >= n:
    count += 1
    n -= max_fear
    fear = fear[0:n]

k = fear.count(1)
count += k

print(count)
