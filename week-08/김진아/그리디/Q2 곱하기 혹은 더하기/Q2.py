S = list(map(int, input()))

result = 0

for i in range(len(S)):
    if i == 0 or S[i] <= 1 or result == 0:
        result += S[i]
    else:
        result *= S[i]

print(result)