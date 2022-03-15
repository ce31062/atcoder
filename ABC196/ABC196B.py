#以下のようにmath.floorを使用するとXの値が大きすぎて誤差が発生してWAとなってしまう
#import math
#x = input()
#print(math.floor(float(x)))

#正解例①
#入力
x = input()
#小数点の位置を探す
index = x.find('.')
#出力
if index == -1:
    print(x)
else:
    print(x[:index])