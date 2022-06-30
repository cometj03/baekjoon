# 서로 다른 부분 문자열의 개수
S = input()
strings = set()
length = len(S)

for i in range(1, length + 1):
    for j in range(length - i + 1):
        strings.add(S[j:j+i])

print(len(strings))