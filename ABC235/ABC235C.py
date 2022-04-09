from collections import defaultdict
N, Q = map(int, input().split())
a = list(map(int, input().split()))

# リストの要素とインデックスを同時に取得するには、enumerate関数を使用する

d = defaultdict(list)
for i, a in enumerate(a, 1):
    d[a].append(i)
# print(d) #defaultdict(<class 'list'>, {1: [1, 2, 5], 2: [3, 6], 3: [4]})

for q in range(Q):
    x, k = map(int, input().split())
    try:
        print(d[x][k-1])
    except IndexError:
        print(-1)