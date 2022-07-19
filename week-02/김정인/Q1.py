# CH4-2. 왕실의 나이트
# 좌표 움직이는 유형 문제는 이동 가능 리스트 만들고 시작
moves = [(1,2), (2,1), (1,-2), (-2,1), (2,-1), (-1,2), (-1,-2), (-2,-1)]
answer = 8

coord = list(input())

# 입력이 소문자로만 들어오는지?
x = int(ord(coord[0]))-96
y = int(coord[1])

for m in moves:
    nextX = x + m[0]
    nextY = y + m[1]
    if nextX < 1 or nextX > 8 or nextY < 1 or nextY > 8:
        answer -= 1

print(answer)

