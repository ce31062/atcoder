N, M, P = map(int, input().split())
cnt = 0
for i in range(M,N+1,P):
#     print(i)
    cnt += 1
print(cnt)