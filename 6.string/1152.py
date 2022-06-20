s = input()
count = s.count(" ") + 1
if s[0] == " ": count -= 1
if s[-1] == " ": count -= 1
print(count)