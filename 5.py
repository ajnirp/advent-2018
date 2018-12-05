def react(string, ignore=None):
    stack = []
    for char in string:
        if char.lower() == ignore:
            continue
        if not stack:
            stack.append(char)
            continue
        if stack[-1].lower() == char.lower() and stack[-1] != char:
            stack.pop()
            continue
        stack.append(char)
    return len(stack)

with open('5.txt', 'r') as f:
    string = f.read().strip()
    print(react(string))
    candidate_chars = set(char.lower() for char in string)
    print(min(react(string, candidate_char) for candidate_char in candidate_chars))