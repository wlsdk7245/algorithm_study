S = list(map(int, input()))

zeroCnt = 0
oneCnt = 0

for i in range(len(S)):
    if i == 0:
        if S[i] == 0:
            zeroCnt += 1
        else:
            oneCnt += 1

    prev = S[i - 1]
    if prev == S[i]:
        continue
    else:
        if prev == 0:
            zeroCnt += 1
        else:
            oneCnt += 1


print(min(zeroCnt, oneCnt))