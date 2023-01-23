a, b = map(int, input().split())

check = False
result = 0

def search(num, count):
    global check, result
    if num == b:
        check = True
        result = count
        return
    elif num >= b:
        return
    search(num * 2, count + 1)
    search(num * 10 + 1, count + 1)

search(a, 1)

if check:
    print(result)
else:
    print(-1)