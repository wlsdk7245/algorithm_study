# Part 2 - Chapter 07 이진 탐색 실전 문제 2 - 떡볶이 떡 만들기
n, m = map(int, input().split())
array = list(map(int, input().split()))

count = 0
length = 0

for i in range(max(array), 0, -1):
    result = 0

    for j in array:
        if (i >= j):
            result += 0
        else:
            result += j - i

    if result >= m:
        length = i
        break

print(length)
