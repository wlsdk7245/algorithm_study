# 실전 2. 위에서 아래로

N = int(input())
numbers = []

for i in range(N):
    numbers.append(int(input()))

numbers.sort()
answer = numbers[::-1]

for a in answer:
    print(a, end = ' ')