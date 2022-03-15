import collections

N = int(input())
l = list(map(int, input().split()))

c = collections.Counter(l)
d = dict(c)
# print(d)

search = 3
for number, mai in d.items():
    if mai == search:
        print(number)