def solution(s):
    result = len(s)

    if len(s) == 1:
        return 1

    for i in range(1, len(s) + 1):
        word = ''
        count = 1
        temp = s[:i]

        for j in range(i, len(s) + i, i):
            if temp == s[j:j + i]:
                count += 1
            else:
                if count != 1:
                    word = word + str(count) + temp
                else:
                    word = word + temp

                temp = s[j:j + i]
                count = 1
        result = min(result, len(word))

    return result