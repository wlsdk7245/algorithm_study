from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

temp = permutations(arr)
result = 0

for numbers in list(temp):
    tempMax = 0

    prev = numbers[0]

    for num in numbers:
        tempMax += abs(prev - num)
        prev = num

    result = max(result, tempMax)

print(result)