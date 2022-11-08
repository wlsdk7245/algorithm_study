S = list(input())
S.sort()

result = ''
num = 0

for i in S:
    if i.isdigit():
        num += int(i)
    else:
        result += i

result += str(num)

print(result)