#座標圧縮の問題
N, M = map(int, input().split())
D = [[] for i in range(N)]

for i in range(M):
    p, y = map(int, input().split())
    D[p-1].append((y, i))

ans = [None]*M
# print(D) #[[(32, 0), (12, 2)], [(63, 1)]]

for i, d in enumerate(D, 1):
    # print(i, d) #0 [(32, 0), (12, 2)], 1 [(63, 1)]
    # print(d) #[(32, 0), (12, 2)], [(63, 1)]
    d.sort()
    # print(d) #[(12, 2), (32, 0)], [(63, 1)]
    for k, (y,j) in enumerate(d):
        ans[j] = str(i).zfill(6) + str(k+1).zfill(6)
print(*ans, sep = "\n")

#print(*ans)とすると，リストの要素がスペース区切りで出力される
#printのオプションsepで，文字の区切りをスペース出なく，改行に指定
#参考URL: https://qiita.com/ryupy/items/38b16a79b1d3f74b959f
