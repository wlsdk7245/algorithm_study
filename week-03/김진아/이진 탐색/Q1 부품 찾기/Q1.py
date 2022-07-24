# Part 2 - Chapter 07 이진 탐색 실전 문제 1 - 부품 찾기
import sys

n = int(input())
stores = list(map(int, sys.stdin.readline().split()))
stores.sort()

m = int(input())
customers = list(map(int, sys.stdin.readline().split()))

def search(array, target, start, end):
    if start > end:
        return 'no'
    mid = (start + end) // 2
    if array[mid] == target:
        return 'yes'
    elif array[mid] > target:
        return search(array, target, start, mid - 1)
    else:
        return search(array, target, mid + 1, end)


for i in customers:
    result = search(stores, i, 0, n - 1)
    print(result, end=" ")
