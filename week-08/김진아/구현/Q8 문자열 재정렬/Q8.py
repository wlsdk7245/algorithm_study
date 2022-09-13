S = list(input())
S.sort()

num = 0
alp = ""

for i in S:
    if i.isalpha():
        alp += i
    else:
        num += int(i)

print(alp + str(num))
