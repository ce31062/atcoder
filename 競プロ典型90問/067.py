N,K = list(map(int,input().split()))

def int2str9(num):
    if num == 0:
        return "0"
    ans = ""
    while num != 0:
        ans = ans + str(num % 9)
        num = num // 9
    return ans[::-1]    #文字列を反転して返す

str_n8 = str(N)

for j in range(K):
    num10=int(str_n8, 8) #8進数→10進数
    str_num9 = int2str9(num10) #10進数→9進数
    str_n8 = str_num9.replace("8","5") #"8"を"5"に変換
print(str_n8)
