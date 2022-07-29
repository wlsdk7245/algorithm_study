# Q27. 정렬된 배열에서 특정 수의 개수 구하기
# 이진탐색 두번?

N, x = map(int, input().split())
array = list(map(int, input().split()))

length = len(array)

def binary_search_start(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        # 제일 왼쪽 인덱스. 수정
        if (array[mid] == target) and (target > array[mid-1] or mid == 0):
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return 0

def binary_search_end(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        # 제일 오른쪽 인덱스
        if (array[mid] == target) and (target < array[mid-1] or mid == N-1) :
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return 0

start = binary_search_start(array, x, 0, length-1)
end = binary_search_end(array, x, 0, length-1)

print(start)
print(end)

answer = end - start + 1

if answer == 0:
    print(-1)
else:
    print(answer)