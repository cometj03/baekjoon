# 괄호
def isValid(s):
    stack = []
    for c in s:
        if c == ")":
            if len(stack) <= 0:
                return False
            stack.pop()
        elif c == "(":
            stack.append(c)
    return True if len(stack) == 0 else False

T = int(input())
while T:
    T -= 1
    if isValid(input()):
        print("YES")
    else:
        print("NO")
    