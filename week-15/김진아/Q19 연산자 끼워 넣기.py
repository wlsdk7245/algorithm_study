from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

minNum = 1e9
maxNum = -1e9

funcList = []

for _ in range(add):
    funcList.append('+')
for _ in range(sub):
    funcList.append('-')
for _ in range(mul):
    funcList.append('x')
for _ in range(div):
    funcList.append('/')

funcList = list(permutations(funcList, N - 1))

def defFunc(result, cur, func):
    if func == '+':
        return result + cur
    elif func == '-':
        return result - cur
    elif func == 'x':
        return result * cur
    elif func == '/':
        if result < 0:
            return -(abs(result) // cur)
        return result // cur

for func in funcList:
    result = arr[0]
    for i in range(N - 1):
        result = defFunc(result, arr[i + 1], func[i])
    minNum = min(minNum, result)
    maxNum = max(maxNum, result)

print(maxNum)
print(minNum)
