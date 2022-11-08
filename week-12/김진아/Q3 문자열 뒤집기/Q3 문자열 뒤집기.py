S = list(map(int, input()))

zeroCnt = 0
oneCnt = 0

prev = 100

for i in range(1, len(S)):
    if prev != S[i]:
        if S[i] == 0:
            oneCnt += 1
        else:
            zeroCnt += 1
    prev = S[i]

print(min(zeroCnt, oneCnt))