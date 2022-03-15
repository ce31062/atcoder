N, M = map(int, input().split())
S = set(map(str, input().split()))
T = set(map(str, input().split()))
C = S & T

for s in S:
    if s in C:
        print("Yes")
    else:
        print("No")