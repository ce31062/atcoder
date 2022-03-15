N = list(input())
N.sort(reverse=True) #リストを降順にsortする
frag = 0
S = []
T = []

for i in range(len(N)):
    if (i % 2) == 0: #偶数ターン
        S.append(N[i])
    else: #奇数ターン
        T.append(N[i])

for j in range(min(len(S), len(T))): #短い方に合わせる
    if S[j] != T[j]:
        S[j], T[j] = T[j], S[j]
        break
S = int("".join(S))
T = int("".join(T))
print(S * T)
