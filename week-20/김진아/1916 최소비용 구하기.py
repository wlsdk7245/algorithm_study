# 첫 시도
# 이게 왜,,, 시간초과인걸까?

from heapq import heappush, heappop

n = int(input())
m = int(input())
arr = [[] for _ in range(n + 1)]

INF = int(1e9)
dist = [INF] * (n + 1)

# arr 배열 각 인덱스에 노드와 비용을 넣음
for _ in range(m):
    x, y, cost = map(int, input().split())
    arr[x].append((y, cost))
start, end = map(int, input().split())

def search(start):
    # start까지의 거리는 0으로 초기화 (자기 자신과의 거리)
    dist[start] = 0
    heap = [[0, start]]

    while heap:
        cost, node = heappop(heap)
        # 기존에 저장된 비용이 더 낫다면 수정할 필요가 없기 때문에 continue
        if dist[node] < cost:
            continue

        # 꺼낸 노드와 연결되어 있는 노드, 비용을 차례대로 검사
        for n, c in arr[node]:
            # 기존 저장된 비용에 꺼낸 노드를 더한다
            ncost = dist[node] + c
            # 그 값이 비용 테이블에 있는 값보다 작으면 비용 테이블을 업데이트하고, 방문처리
            if dist[n] > ncost:
                dist[n] = ncost
                heappush(heap, [ncost, n])

search(start)
print(dist[end])
