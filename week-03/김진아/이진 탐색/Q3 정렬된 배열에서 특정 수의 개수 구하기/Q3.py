# Part 2 - Chapter 07 이진 탐색 1 - 정렬된 배열에서 특정 수의 개수 구하기
n, x = map(int, input().split())
arr = list(map(int, input().split()))

count = 0

def search(array, target, start, end):
    global count
    if start > end:
        return -1

    mid = (start + end) // 2
    if array[mid] == target:
        count += 1
        search(array, target, start, mid - 1)
        search(array, target, mid + 1, end)
    elif array[mid] > target:
        search(array, target, start, mid - 1)
    else:
        search(array, target, mid + 1, end)

search(arr, x, 0, n - 1)

if count == 0:
    print(-1)
else:
    print(count)
