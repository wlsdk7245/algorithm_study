n, m = map(int, input().split())

dna = [input() for _ in range(n)]

result = ''
cnt = 0

for k in range(m):
    Acnt = 0
    Ccnt = 0
    Gcnt = 0
    Tcnt = 0

    for i in range(n):
        if dna[i][k] == 'A':
            Acnt += 1
        if dna[i][k] == 'C':
            Ccnt += 1
        if dna[i][k] == 'G':
            Gcnt += 1
        if dna[i][k] == 'T':
            Tcnt += 1
    maxCnt = max(Acnt, Ccnt, Gcnt, Tcnt)
    cnt += n - maxCnt

    if maxCnt == Acnt:
        result += 'A'
        continue
    elif maxCnt == Ccnt:
        result += 'C'
        continue
    elif maxCnt == Gcnt:
        result += 'G'
        continue
    elif maxCnt == Tcnt:
        result += 'T'
        continue

print(result)
print(cnt)