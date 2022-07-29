# Part 2 - Chapter 06 정렬 실전 문제 1 - 위에서 아래로
n = int(input())
num = [int(input()) for i in range(n)]

num.sort(reverse=True)

for i in num:
    print(i, end=' ')