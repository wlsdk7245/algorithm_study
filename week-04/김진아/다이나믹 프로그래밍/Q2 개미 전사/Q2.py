n = int(input())

k = list(map(int, input().split()))

odd = 0
even = 0

for i in range(len(k)):
    if i % 2 == 0:
        even += k[i]
    else:
        odd += k[i]

print(max(odd, even))
