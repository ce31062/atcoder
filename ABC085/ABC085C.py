#TLE
N, Y = map(int, input().split())
index = 0
for x in range(N+1):
    for y in range(N+1):
            if x + y + (N-x-y) == N and (10000*x + 5000*y + 1000*(N-x-y)) == Y and index == 0:
                print(x, y, (N-x-y))
                index = 1
if index == 0:
    print(-1, -1, -1)