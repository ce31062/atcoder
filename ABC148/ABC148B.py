N = int(input())
S, T = map(str, input().split())
ans = ""

for n in range(N):
    ans += S[n]
    ans += T[n]
print(ans)