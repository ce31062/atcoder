n = input()
# print("文字数", len(n))
# print("N:",n)
# print("reverseN:",n[::-1])
if n == n[::-1]:
    print("Yes")
else:
    for i in range(len(n)):
        if n[-1-i] == '0':
            n = '0' + n
        else:
            break
    # print(n)
    if n == n[::-1]:
        print("Yes")
    else:
        print("No")
#回答例
S=input()
for i in range(10):
	T = "0"*i + S
 	if T==T[::-1]:
 		print("Yes")
 		exit()
print("No")