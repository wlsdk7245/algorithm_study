# 실전4. 두 배열의 원소 교체
N, K  = map(int, input().split())
A= list(map(int, input().split()))
B= list(map(int, input().split()))

# A 합이 최대. 최소(A) < 최대(B)일때까지 최대 k번 교체. 정렬 먼저
A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        temp = A[i]
        A[i] = B[i]
        B[i] = temp
    else:
        break

print(sum(A))