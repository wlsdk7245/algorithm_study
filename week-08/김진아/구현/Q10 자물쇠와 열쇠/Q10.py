def attach(i, j, m, rotatedKey, locks):
    for a in range(m):
        for b in range(m):
            locks[a + i][b + j] += rotatedKey[a][b]


def check(locks, m, n):
    for i in range(n):
        for j in range(n):
            if locks[m + i][m + j] != 1:
                return False
    return True


def detach(i, j, m, rotatedKey, locks):
    for a in range(m):
        for b in range(m):
            locks[a + i][b + j] -= rotatedKey[a][b]


def rotate(arr):
    n = len(arr)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - i - 1] = arr[i][j]
    return result


def solution(key, lock):
    m = len(key)
    n = len(lock)

    locks = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            locks[n + i][n + j] = lock[i][j]

    rotatedKey = key

    for _ in range(4):
        rotatedKey = rotate(rotatedKey)
        for i in range(1, m + n):
            for j in range(1, m + n):
                attach(i, j, m, rotatedKey, locks)
                if (check(locks, m, n)):
                    return True
                detach(i, j, m, rotatedKey, locks)

    return False