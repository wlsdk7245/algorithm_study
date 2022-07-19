# CH12-Q8. 문자열 재정렬
inputStr = input()
sum = 0
answer = []

for i in inputStr:
    if i.isdigit():
        sum += int(i)
    else:
        answer.append(i)

answer.sort()

# 수정. 숫자가 하나도 없어서 sum이 0 인 경우도 고려해야 함
if sum != 0:
    answer.append(str(sum))

print(''.join(answer))

