# 카드 2
n = int(input())
lst = [i for i in range(1, n+1)]

while len(lst) > 1:
    newlst = []
    if len(lst) % 2 == 1:
        newlst.append(lst[-1])
    newlst += lst[1::2]
    lst = newlst[:]
print(lst[0])