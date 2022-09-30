s = input()

num = []
ops = []

n = ''

for i in s:
    if i in ('+', '-'):
        ops.append(i)
        num.append(int(n))
        n = ''
    else:
        n += i

num.append(int(n))

result = num[0]
isPlus = True

for i in range(len(ops)):
    if isPlus:
        if ops[i] == "+":
            result += num[i + 1]
        else:
            result -= num[i + 1]
            isPlus = False
    else:
        result -= num[i + 1]

print(result)