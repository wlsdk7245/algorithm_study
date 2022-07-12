N, M, K = map(int, input().split())
dataSet = list(map(int, input().split()))
dataSet.sort(reverse=True)

result = 0
# plusCount는 더한 횟수를 카운팅할 변수로 M과 비교하여 사용
plusCount = 0

while plusCount < M:
    for j in range(K):
        if plusCount == M:
            break
        result += dataSet[0]
        plusCount += 1

    if plusCount == M:
        break
    result += dataSet[1]
    plusCount += 1

print(result)