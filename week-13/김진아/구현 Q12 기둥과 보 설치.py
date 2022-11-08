def check(answer):
    for x, y, a in answer:
        if a == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif a == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    print(build_frame)
    for item in build_frame:
        x, y, a, b = item

        # 설치
        if b == 1:
            answer.append([x, y, a])
            if not check(answer):
                answer.remove([x, y, a])
        # 삭제
        else:
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])
    answer.sort()
    print(answer)
    return answer