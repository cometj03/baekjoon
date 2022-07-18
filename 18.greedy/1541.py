# 잃어버린 괄호
math = input()
nums = [*map(int, math.replace("-", "+").split("+"))] # 숫자 추출
op = []
ans = nums[0]

for i in math:
    if i == "+" or i == "-":
        op.append(i)

minus = False
for i in range(1, len(nums)):
    if minus or op[i-1] == "-":
        minus = True
        ans -= nums[i]
    elif op[i-1] == "+":
        ans += nums[i]

print(ans)