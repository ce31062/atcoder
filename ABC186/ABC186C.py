N = int(input())
s = "7"
ans = 0

for n in range(1, N+1):
    oct1 = oct(n)
    if (s in str(oct1)) or (s in str(n)):
        ans += 1

print(N- ans)