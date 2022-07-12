# 02 숫자 카드 게임

n,m = map(int, input().split())

result = 0

for _ in range(m):
    num = list(map(int, input().split()))
    mini = min(num)

    result = max(result,mini)


print(result)
