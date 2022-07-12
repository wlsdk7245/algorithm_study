N, M = map(int, input().split())
matrix = list()
card = 0

for _ in range(N):
    matrix.append(list(map(int, input().split())))

for i in range(len(matrix)):
    if card <= min(matrix[i]):
        card = min(matrix[i])

print(card)

