# 듣보잡
n, m = map(int, input().split())
notlistened = {input() for _ in range(n)}
notseen = {input() for _ in range(m)}
ans = notlistened & notseen

print(len(ans))
for name in sorted(list(ans)):
    print(name)