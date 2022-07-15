# 프린터 큐
T = int(input())
while T:
    T -= 1
    n, m = map(int, input().split())
    docs = [*map(int, input().split())]
    q = [0]*n
    # 튜플의 첫 번째는 인덱스, 두 번째는 값
    for i, x in enumerate(docs):
        q[i] = (i, x)

    tmp = (-1, -1)
    count = 0
    while tmp[0] != m:
        maxitem = max(q, key=lambda x: x[1])
        while maxitem[1] != q[0][1]:
            q.append(q.pop(0))
        tmp = q.pop(0)
        count += 1
    print(count)