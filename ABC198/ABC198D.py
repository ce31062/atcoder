#わからん！！
from itertools import permutations
#itertoolsは効率的なループ処理のためのイテレータ関数
#
def StoL(S, num):
    # 文字列Sをnum[c]対応表にしたがって数値に変換する
    ret = 0
    for s in S:
        ret *= 10
        ret += num[s]
    return ret

S1, S2, S3 = input(), input(), input()
S = list(set(S1) | set(S2) | set(S3))  # S: S1~S3に登場する文字(重複なし)
nonzero = set([S1[0], S2[0], S3[0]])  # nonzero: S1~S3の先頭(重複なし)
L = len(S)  # L: 文字の種類数
# 以下、itertools.permutationsにより0~9の数字をL種類の文字に当てはめた全パターンを求める。
# permutations(n, r) は n < r のとき1回もiterateせずにfor文を抜ける。

for P in permutations(range(10), L): #第一引数には0~9のイテラブル
    num = {}  # num[c]: 文字cに対応する数字
    for i, p in enumerate(P):
        num[S[i]] = p
    if any(num[z] == 0 for z in nonzero):  # S1~S3の先頭文字が0だった場合はスキップ
        continue
    else:
        s1 = StoL(S1, num)
        s2 = StoL(S2, num)
        s3 = StoL(S3, num)
        if s1 + s2 == s3:
            print(s1)
            print(s2)
            print(s3)
            exit()
print('UNSOLVABLE')

#集合を扱う(set型)
# A = {1, 2, 3}
# B = {1, 4, 5}
# print(A | B) #和集合
# print(A & B) #積集合
# print(A - B) #差集合
# print(A ^ B) #排他的論理和集合
# print(list(A)) #集合→リスト変換

#リストから順列を生成、列挙
# l = ['a', 'b', 'c', 'd']
# for v in permutations(l,2): #第一引数にイテラブル、第二引数に選択する個数
#     print(v)