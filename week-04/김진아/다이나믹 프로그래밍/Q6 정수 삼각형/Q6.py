n = int(input())
triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(1, n):
    m = len(triangle[i])
    for j in range(m):
        if j == 0:
            left = 0
        else:
            left = triangle[i-1][j-1]
        if j == m - 1:
            right = 0
        else:
            right = triangle[i-1][j]
        num = max(left, right)
        triangle[i][j] += num

print(max(triangle[n-1]))