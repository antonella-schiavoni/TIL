def isValid(s: str) -> bool:
    stack = []
    closing = ["]", ")", "}"]
    opening = ["[", "(", "{"]
    close_to_open = {"]": "[", ")": "(", "}": "{"}
    if len(s) == 1:
        return False
    for char in s:
        if char in opening:
            stack.append(char)
        if char in closing:
            if len(stack) == 0:
                return False
            else:
                last_elem = stack[-1]
                if last_elem != close_to_open[char]:
                    return False
                stack.pop()
    if stack:
        return False
    return True


if __name__ == "__main__":
    s = "{[]}"
    isValid(s)
