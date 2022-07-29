# 실전 3. 떡볶이 떡 만들기(해설)

N, M = list(map, input().split(' '))
cm = list(map(int, input().split()))

start = 0
end = max(cm)
answer = 0

# 이진탐색
while(start <= end):
    mid = (start + end) //2
    sumLen = 0
    # 현재 설정한 절단기 높이에서 자르고 남은 떡 합 구해보기
    for c in cm:
        if c > mid:
            sumLen += c - mid
    # 모질라면 절단기 높이 감소
    if sumLen < M:
        end = mid - 1
    # 남으면 절단기 높이 증가. 단, 정확히 일치하지 않을 수도 있는데 그때는 남는게 맞으니까 저장 먼저하고 넘어가기
    else:
        answer = mid
        start = mid + 1

print(answer)