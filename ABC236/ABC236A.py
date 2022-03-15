S = input()
a,b = map(int, input().split())
ans = ""
for i in range(len(S)):
    if i+1 == a:
        ans += S[b-1]
    elif i+1 == b:
        ans += S[a-1]
    else:
        ans += S[i]

print(ans)