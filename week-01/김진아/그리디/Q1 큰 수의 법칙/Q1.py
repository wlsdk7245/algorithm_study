## N, M, K 입력받기
n, m, k = map(int, input().split())

# N개의 자연수 입력받기
data = list(map(int, input().split()))
# 큰 수부터 내림차순 정렬하기
data.sort(reverse=True)

a, b = data[0], data[1]

result = (k * a + b) * (int(m / (k + 1))) + (m % (k + 1)) * a

print(result)

# ## N, M, K 입력받기
# n, m, k = map(int, input().split())
#
# # N개의 자연수 입력받기
# data = list(map(int, input().split()))
# # 큰 수부터 내림차순 정렬하기
# data.sort(reverse=True)
#
# result = 0
# count = 0
#
# for i in range(m):
#     if count == k:
#         result += data[1]
#         count = 0
#     else:
#         result += data[0]
#         count += 1
#
# print(result)
#