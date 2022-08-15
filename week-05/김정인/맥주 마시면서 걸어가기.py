# 실버1. 맥주 마시면서 걸어가기
# 제목은 마음에 드는데... 힘드네요...
# 솔직히... 머리가 넘 아파서 코드 해설만 봤어... 이정도는 봐줘잉><

from collections import deque

bfs(sx, sy):
    queue = deque([(sx, sy)])   # 출발지점 넣기
    visited[(sx, sy)] = False    # 출발지점 방문 처리
    while queue:
        x, y = queue.popleft()  # 좌표 하나 빼
        if abs(ex-x) + abs(ey-y) <= 1000:   # 현재 지점에서 도착지점까지 맥주 20개로 갈 수 있다면
            return 'happy'  # 'happy' 출력

        for i in range(len(cu)):
            cu_x = cu[i][0] # 편의점 가보기
            cu_y = cu[i][1]
            # 현재 편의점에서 목적지까지 맥주 20개로 갈 수 있고 방문해본 편의점이 아니라면
            if abs(cu_x-x) + abs(cu_y-y) <= 1000 and visited.get((cu_x, cu_y), True):
                visited[(cu_x, cu_y)] = False   # 방문처리
                queue.append((cu_x, cu_y))      # 방문해보자 queue에 넣어
    return 'sad'    # 출발 그리고 편의점에서도 맥주 20개로 목적지까지 못가면 'sad'


tc = int(input())
for tc_n in range(1, tc+1):
    n = int(input())    # 편의점 개수

    sx, sy = map(int, input().split())  # 출발 좌표
    cu = [] # 편의점 좌표 저장
    for i in range(n):
        cu.append(list(map(int, input().split())))
    ex, ey = map(int, input().split())  # 페스티벌 좌표

    visited = {}

    print(bfs(sx, sy))