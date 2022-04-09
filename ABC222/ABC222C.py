# https://qiita.com/u2dayo/items/a817a680c1c1687ced54#c%E5%95%8F%E9%A1%8Cswiss-system-tournament
N, M = map(int, input().split())
hands = []
for _ in range(2 * N):
        s = input()
        hands.append(s)

# ランキング管理用の配列(★)
rank = [[0, i] for i in range(2*N)] #この内包の書き方は覚える

# じゃんけんゲームの実装
# D[h1][h2]: じゃんけんでh1, h2を出して、あいこなら0, h1が勝つなら1, h2が勝つなら2
# 辞書の要素に辞書を追加する方法(★)
D = {"G": {"G": 0, "C": 1, "P": 2},
     "C": {"C": 0, "P": 1, "G": 2},
     "P": {"P": 0, "G": 1, "C": 2}}
# print(D["G"]["C"]) #1

for j in range(M): # Round
        for i in range(N): # 対戦カード
                p1 = rank[2 * i][1] #2*i位の選手番号
                p2 = rank[2 * i + 1][1] #2*i+1位の選手番号
                h1 = hands[p1][j] #p1がjラウンド目に出す手
                h2 = hands[p2][j] #p2がjラウンド目に出す手
                winner = D[h1][h2]
                if winner == 0: #あいこ
                    continue
                elif winner == 1: # p1の勝利
                    rank[2*i][0] -= 1 # p1の勝利ポイントに-1
                else: # p2の勝利
                    rank[2*i+1][0] -= 1 # p1の勝利ポイントに-1
        rank.sort() #1ラウンドが終わったら勝利ポイントが小さい順に並び変える。同じなら選手番号が小さい順が上

for i in range(2*N):
    print(rank[i][1]+1)