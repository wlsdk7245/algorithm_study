a, b = map(int, input().split())

result = -1

def search(num, count):
    global result
    if num == b:
        result = count
        return
    elif num >= b:
        return
    search(num * 2, count + 1)
    search(num * 10 + 1, count + 1)

search(a, 1)

print(result)