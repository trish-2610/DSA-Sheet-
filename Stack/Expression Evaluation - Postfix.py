def evaluate_expression(expr) -> int:
    stack = []
    for char in expr.split():
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == "+" : stack.append(a+b)
            elif char == "-" : stack.append(a-b)
            elif char == "*" : stack.append(a*b)
            elif char == "/" : stack.append(int(a/b))
    return stack.pop()
print(evaluate_expression("5 6 2 + * 12 4 / -"))