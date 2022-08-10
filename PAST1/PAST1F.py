S = input()
N = len(S)
words = []

i = 0 #iは単語を切り抜く始点
while i < N:
    j = i + 1 #jは単語を切り抜く終点
    while j < N and S[j].islower(): #小文字である限り実行
        j += 1
    words.append(S[i:j+1])
    i = j + 1

# print(words) #['FisH', 'DoG', 'CaT', 'AA', 'AaA', 'AbC', 'AC']

words.sort(key=str.lower)
print("".join(words))