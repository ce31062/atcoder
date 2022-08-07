H, W = map(int, input().split())

if W == 1 or H == 1:
    print(H*W)
    exit()
elif W % 2 == 0:
    tmp_w = W // 2
else:
    tmp_w = (W//2)+1

tmp_h = H // 2 #無視してよい行


print(tmp_w * (H - tmp_h) )

