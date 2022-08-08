T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    gold = []

    for i in range(n):
        gold.append(arr[m * i:m * i + m])

    for i in range(1, m):
        for j in range(n):
            if j == 0:
                a = 0
            else:
                a = gold[j - 1][i - 1]

            b = gold[j][i - 1]

            if j == n - 1:
                c = 0
            else:
                c = gold[j + 1][i - 1]

            num = max(a, b, c)
            gold[j][i] = gold[j][i] + num

    maxNum = 0
    for i in range(n):
        maxNum = max(maxNum, gold[i][m - 1])

    print(maxNum)