r, x, y = map(int, input().split())
l = (x**2 + y**2)**0.5
sho = l // r
amari = l % r
# print("距離",l)
# print("1歩で進む距離",r)
# print("直線歩数",sho)
# print("残り距離", l-sho*r)
# print("計算あまり",amari)
if amari == 0.0:
    print(int(sho))
else:
    if sho ==0:
        print(2)
    else:
    # print(f"残りの距離は{l - r * int(sho-1)}です。")
        print(int(sho)+1)

# 模範回答例
import math
R,X,Y=map(int,input().split())
D=math.sqrt(X*X+Y*Y)
if D==R:
    print(1)
elif D<=R+R:
    print(2)
else:
    print(math.ceil(D/R))
