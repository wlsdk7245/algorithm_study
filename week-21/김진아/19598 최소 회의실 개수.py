import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()

ends = [0]

for start, end in arr:
    if start >= ends[0]:
        heapq.heappushpop(ends, end)
    else:
        heapq.heappush(ends, end)

print(len(ends))