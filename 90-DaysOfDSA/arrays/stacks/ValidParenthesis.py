s = "{[[]]]}"

def isValid(s):
    stack = []
    hashmap = {"}":"{","]":"[",")":"("}
    for c in s:
        if c in hashmap:
            if stack and stack[-1]==hashmap[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False
        
print(isValid(s))
