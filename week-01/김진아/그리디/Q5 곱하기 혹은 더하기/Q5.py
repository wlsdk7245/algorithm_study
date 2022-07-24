s = list(map(int, input()))

result = 0

for i in range(len(s)):
    if s[i] == 0 or i == 0 or result == 0:
        result += s[i]
    else:
        result *= s[i]

print(result)
