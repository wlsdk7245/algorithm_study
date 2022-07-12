# GREEDY 01 큰 수의 법칙

n, m, k = map(int, input().split())

num = list(map(int, input().split()))

num.sort()

maxi = num[n-1]
maxi2 = num[n-2]

result = 0

while m >= (k+1):
    result += maxi * k
    result += maxi2
    m-(k+1)

if m < k:
    result += maxi * m


print(result)
    
