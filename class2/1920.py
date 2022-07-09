# 수 찾기
n = int(input())
A = {*input().split()}
m = int(input())
for x in input().split():
    print(int(x in A))