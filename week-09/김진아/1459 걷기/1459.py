x, y, w, s = map(int, input().split())

m1 = (x + y) * w # 평행 이동

# 짝수, 홀수에 따른 이동
if (x + y) % 2 == 0: # 짝수라면
    m2 = max(x, y) * s # 대각선으로만 이동
else: # 홀수라면
    m2 = (max(x, y) - 1) * s + w # 대각선이동 + 평행이동 1번

# 대각선 + 평행 이동
m3 = (min(x, y) * s) + (abs(x - y) * w)

print(min(m1, m2, m3))
