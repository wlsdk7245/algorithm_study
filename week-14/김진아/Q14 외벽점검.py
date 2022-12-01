from itertools import permutations

def solution(n, weak, dist):
    leng = len(weak)
    for x in range(leng):
        weak.append(weak[x] + n)

    answer = len(dist) + 1

    for start in range(leng):
        for friends in list(permutations(dist, len(dist))):
            count = 0
            position = weak[start] - friends[count - 1]

            for index in range(start, start + leng):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer