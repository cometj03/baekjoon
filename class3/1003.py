# 피보나치 함수
T = int(input())
zero = [1] + [0] * 40
one = [0, 1] + [0] * 40

for i in range(2, 41):
    zero[i] = zero[i-1] + zero[i-2]
    one[i] = one[i-1] + one[i-2]

while T:
    T -= 1
    n = int(input())
    print(zero[n], one[n])