def solution(s):
    answer = 100000000

    for i in range(1, len(s) // 2 + 2):
        res = ''
        count = 1
        temp = s[:i]

        for j in range(i, len(s) + i, i):
            if temp == s[j:i + j]:
                count += 1
            else:
                if count == 1:
                    res += temp
                else:
                    res += str(count) + temp
                temp = s[j: i + j]
                count = 1

        answer = min(answer, len(res))

    return answer