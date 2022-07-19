# CH12-Q7. 럭키 스트레이트
left = 0
right = 0


N = input()
index = len(N)//2

for i in range(0,index):
    left += int(N[i])

for i in range(index, len(N)):
    right += int(N[i])

if left == right:
    print("LUCKY")
else:
    print("READY")

