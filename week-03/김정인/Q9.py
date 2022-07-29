# Q28. 고정점 찾기
# 인덱스랑 값 비교해서 인덱스 < 값이면 왼쪽, 반대면 오른쪽 탐색

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return None

N = int(input())
array = list(map(int, input().split()))

answer = binary_search(array, 0, N-1)

if answer == None:
    print(-1)
else:
    print(answer)