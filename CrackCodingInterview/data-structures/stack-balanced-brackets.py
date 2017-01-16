def is_matched(expression):
    """
    Inputs to lookout for:
        - single input: [, ], (, )
        - right side's length is greater: [[([()
        - left side's length is greater: ([})))]

    """
    stack = []
    for c in expression:
        if c == "{": stack.append("}")
        elif c == "[": stack.append("]")
        elif c == "(": stack.append(")")
        else:
            if len(stack) < 1:
                return False

            tos = stack.pop()
            if tos == c:
                continue
            else:
                return False

    if len(stack) > 0:
        return False
    else:
        return True

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
