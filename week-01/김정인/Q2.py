inputList = list(map(int,input()))
answer = inputList[0]

for i in range(0, len(inputList)-1):
    if answer<=1 or int(inputList[i+1])<=1:
        answer += int(inputList[i+1])
    else:
        answer *= int(inputList[i+1])

print(answer)
