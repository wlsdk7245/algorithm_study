# from itertools import combinations
#
# n, m = map(int, input().split())
# k = list(map(int, input().split()))
#
# result = list(combinations(k, 2))
# print(result)

# 처음에 조합으로 풀려고 했는데 실패 => 왜 안되는지 이해 X

n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

for x in data:
    array[x] += 1

result = 0

for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n

print(result)
