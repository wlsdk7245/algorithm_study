n, newScore, p = map(int, input().split())
res = 0

if n == 0:
    print(1)
else:
    score = list(map(int, input().split()))
    if n == p and score[-1] >= newScore:
        print(-1)
    else:
        res = n + 1
        for i in range(n):
            if score[i] <= newScore:
                res = i + 1
                break
        print(res)
