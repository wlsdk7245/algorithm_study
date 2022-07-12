# Q1. 모험가 길드

N = int(input())
adventurer = list(map(int, input().split()))
members = 0
answer = 0

adventurer.sort()

for a in adventurer:
    members += 1
    if a <= members:
        answer += 1
        members = 0

print(answer)