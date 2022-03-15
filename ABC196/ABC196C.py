n = int(input())
i = '1'
ans = 0
while(True):
    if int(i + i) <= n:
        ans += 1
    else:
        break
    i = str(int(i) + 1)

print(ans)