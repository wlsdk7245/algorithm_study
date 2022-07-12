import heapq

case = int(input())
heap = []
a = 0
b = 0
count = 0
for _ in range(case):
    heapq.heappush(heap, int(input()))

last = len(heap)-1
for i in range(len(heap)):
    if len(heap) == 1:
        break

    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    count += a+b
    heapq.heappush(heap, a+b)

print(count)
