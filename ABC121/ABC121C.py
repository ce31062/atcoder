N, M = map(int, input().split())
l = []
sum = 0
m = 0

for n in range(N):
    A, B = map(int, input().split())
    l.append([A,B])

l.sort()

for i in range(N):
    # print(M-m) #残り購入数量
    if (M-m) - l[i][1] >= 0:
        m += l[i][1]
        sum += l[i][1] * l[i][0]
    else:
        sum += l[i][0] * (M-m)
        break

print(sum)