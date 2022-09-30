n = int(input())
k = int(input())

arr = list(map(int, input().split()))
arr.sort()

diff = []

for i in range(len(arr) - 1):
    diff.append(arr[i + 1] - arr[i])

diff.sort()

while k-1:
    if len(diff) == 0:
        break
    diff.pop()
    k -= 1

print(sum(diff))
