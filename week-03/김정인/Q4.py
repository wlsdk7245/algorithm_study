# Q23. 국영수

N = int(input())
students = []

for i in range(N):
    students.append(input().split())

# 내림차순은 -로(해설 참고)
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for s in students:
    print(s[0])