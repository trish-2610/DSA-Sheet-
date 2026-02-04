def valid_parentheses(expr) -> bool:
    stack = []
    pairs = { "}":"{",
              "]":"[",
              ")":"("
            }
    for char in expr:
        if char in "{[(":
            stack.append(char)
        elif char in "}])":
            if not stack or stack[-1] != pairs[char]:
                return False
            else :
                stack.pop()
    return not stack
print(valid_parentheses("])}"))
