import sys
input = sys.stdin.readline

T = int(input())

d = [0] * 12
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 12):
    d[i] = d[i - 3] + d[i - 2] + d[i - 1]

for _ in range(T):
    n = int(input())
    print(d[n])

# import sys
# input = sys.stdin.readline
#
# T = int(input())
#
# def solution():
#     n = int(input())
#     d = [0] * (n + 1)
#
#     d[1] = 1
#     d[2] = 2
#     d[3] = 4
#
#     print(d)
#
#     for i in range(4, n + 1):
#         print(i, d[i])
#         d[i] = d[i - 3] + d[i - 2] + d[i - 1]
#
#     print(d[n])
#
# for _ in range(T):
#     solution()
