# Q24. 안테나

N = int(input())
house = list(map(int, input().split()))

house.sort()
best = house[(N-1)//2]

print(best)