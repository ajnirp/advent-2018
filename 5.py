# python3 5.py < 5.txt
with open(0) as file:
    data = file.read().strip()

def react(s):
    stack = []
    for char in s:
        if stack and abs(ord(char) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(char)
    return len(stack)

def best_react(s):
    types = set(c.lower() for c in s)
    result = 1e10
    for char in types:
        candidate = react(c for c in s if c.lower() != char)
        result = min(result, candidate)
    return result

print(react(data))
print(best_react(data))
