N, M, Q = map(int, input().split())

G = [[] for _ in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
# print(G) #[[1], [0, 2], [1]]　これがグラフの基本形

#初期の色情報
col = list(map(int, input().split()))

#クエリを処理する
for s in range(Q):
    t, x, *y = map(int, input().split())
    x -= 1
    print(col[x]) #全クエリ共通処理
    if t == 1:
        for v in G[x]:
            col[v] = col[x]
    else:
        col[x] = y[0]