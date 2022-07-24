# Part 3 - Chapter 06 정렬 2 - 안테나
n = int(input())

location = list(map(int, input().split()))
location.sort()

print(location[int(n/2) - 1])