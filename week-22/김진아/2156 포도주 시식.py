import sys
input = sys.stdin.readline

n = int(input())
w = [0] * 10001
for i in range(n):
    w[i] = int(input())
d = [0] * 10001

# d[0] = w[0]
# d[1] = w[0] + w[1]
# d[2] = max(d[0] + w[2], d[1], w[1] + w[2])
# d[3] = max(w[3] + d[0] + w[2], w[3] + d[1], d[2])

d[0] = w[0]
d[1] = w[0] + w[1]
d[2] = max(d[0] + w[2], d[1], w[1] + w[2])

for i in range(3, n):
    d[i] = max(w[i] + d[i - 3] + w[i - 1], w[i] + d[i - 2], d[i - 1])

print(max(d))