# 실전 2. 부품 찾기

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

N = int(input())
all = list(map(int, input().split()))

M = int(input())
request = list(map(int, input().split()))

all.sort()

for r in request:
    answer = binary_search(all, r, 0, N-1)
    if answer == None:
        print('no', end = ' ')
    else:
        print('yes', end=' ')