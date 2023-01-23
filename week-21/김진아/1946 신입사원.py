import sys
input = sys.stdin.readline

T = int(input())

def solution():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    arr.sort()
    temp = arr[0][1]
    result = 1

    # 서류심사 성적을 기준으로 정렬을 해두면, 면접심사 성적만 비교하면 된다.
    # 면접심사 성적이 앞에 나온 성적보다 낮은 게 있다면 무조건 탈락이다.
    for i in range(1, n):
        if temp > arr[i][1]:
            result += 1
            temp = arr[i][1]
    return result

for _ in range(T):
    print(solution())