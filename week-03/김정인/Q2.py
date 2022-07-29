# 실전3. 성적이 낮은 순서로 학생 출력하기

N = int(input())
students = []

for i in range(N):
    temp = input().split()
    students.append((temp[0], temp[1]))

def setting(data):
    return data[1]

answer = sorted(students, key=setting)

for a in answer:
    print(a[0], end=' ')
