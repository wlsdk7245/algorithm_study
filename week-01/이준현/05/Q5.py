number = list()
s = input()
result = 0

for i in s:
    number.append(int(i))

for i in number:
    if i == 0 or i == 1 or result == 0 or result == 1:
        result += i
    else:
        result *= i

print(result)
