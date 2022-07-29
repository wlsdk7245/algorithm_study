# Part 2 - Chapter 06 정렬 실전 문제 2 - 성적이 낮은 순서로 학생 출력하기
n = int(input())
score = [input().split() for i in range(n)]
score.sort(key=lambda data: int(data[1]))

for person in score:
    print(person[0], end=" ")

# 문제가 어렵지 않아서 코드 간결화에 집중함!