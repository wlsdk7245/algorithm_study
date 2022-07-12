# GREEDY 02. 곱하기 혹은 더하기


data = list(map(int, input()))

result = 0

for i in range(len(data)):

    if i == 0:
        if data[i] == 0:
            result += data[i]
        
        elif data[i+1] == 0:
            result += data[i]

        else :
            result += (data[i] * data[i+1])

    else :
        if data[i] ==0 or result == 0:
            result += data[i]

        else :
            result *= data[i]





print(result)

        
