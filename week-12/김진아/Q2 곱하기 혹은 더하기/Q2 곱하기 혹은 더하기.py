S = list(map(int, input()))

result = S[0]

for i in range(1, len(S)):
    prev = S[i - 1]
    if prev == 0 or S[i] == 0:
        result += S[i]
    else:
        result *= S[i]

print(result)