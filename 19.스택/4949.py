# 균형잡힌 세상
def isBalanced(string):
    stack = []
    for c in string:
        if (c == ")" or c == "]") and len(stack) <= 0:
            return False
        if c == ")":
            if stack.pop() != "(":
                return False
        if c == "]":
            if stack.pop() != "[":
                return False
        if c == "(" or c == "[":
            stack.append(c)
    return True if len(stack) == 0 else False

while True:
    s = input()
    if s == ".":
        break
    if isBalanced(s):
        print("yes")
    else:
        print("no")
