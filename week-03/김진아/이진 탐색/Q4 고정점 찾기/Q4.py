# Part 3 - Chapter 15 이진 탐색 2 - 고정점 찾기
n = int(input())
arr = list(map(int, input().split()))

def search(array, start, end):
    mid = (start + end) // 2
    if start > end:
        return None
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return search(array, start, mid - 1)
    else:
        return search(array, mid + 1, end)

result = search(arr, 0, n - 1)

if result == None:
    print(-1)
else:
    print(result)