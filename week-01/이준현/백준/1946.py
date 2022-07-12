import sys

case = int(input())
for _ in range(case):
    number = int(input())
    interviewers = list()
    count = 1
    for _ in range(number):
        man = list(map(int, sys.stdin.readline().split()))
        interviewers.append(man)
    interviewers.sort()
    k = interviewers[0][1]
    for i in range(1, number):
        if k > interviewers[i][1]:
            count += 1
            k = interviewers[i][1]
    print(count)
