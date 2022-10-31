n = int(input())
arr = []

one = 0
two = 0

timeOne = 0
timeTwo = 0

prev = 0

for _ in range(n):
    a, b = input().split()
    c, d = map(int, b.split(":"))

    if one > two:
        timeOne += c * 60 + d - prev
    elif one < two:
        timeTwo += c * 60 + d - prev

    prev = c * 60 + d

    if int(a) == 1:
        one += 1
    else:
        two += 1

if one > two:
    timeOne += 48 * 60 - prev
elif one < two:
    timeTwo += 48 * 60 - prev

print('{:0>2}:{:0>2}'.format(timeOne//60, timeOne % 60))
print('{:0>2}:{:0>2}'.format(timeOne//60, timeOne % 60))

# print(str(timeOne // 60) + ':' + str(timeOne % 60))
# print(str(timeTwo // 60) + ':' + str(timeTwo % 60))
#