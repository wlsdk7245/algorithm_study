num = list(input())

result = 0

for i in range(len(num)):
    if i == 0 or int(num[i]) <= 1 or result == 0:
        result += int(num[i])
    else:
        result *= int(num[i])

print(result)



