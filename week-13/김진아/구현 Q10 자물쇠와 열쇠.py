def rotate(arr):
    n = len(arr)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - i - 1] = arr[i][j]
    return result


def check(arr):
    n = len(arr) // 3

    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if arr[i][j] != 1:
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)

    locks = [[0] * (n * 3) for _ in range(n * 3)]

    # 자물쇠 새로운 배열에 저장
    for i in range(n):
        for j in range(n):
            locks[n + i][n + j] = lock[i][j]

    # 열쇠를 동서남북 네 방향 회전시키며 하나씩 확인
    for _ in range(4):
        key = rotate(key)
        for i in range(1, m + n):
            for j in range(1, m + n):
                for x in range(m):
                    for y in range(m):
                        locks[x + i][y + j] += key[x][y]

                if check(locks):
                    return True

                for x in range(m):
                    for j in range(m):
                        locks[x + i][y + j] -= key[x][y]

    return False