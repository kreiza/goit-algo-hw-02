def check_brackets(expression):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != pairs[char]:
                return "Несиметрично"
            stack.pop()

    return "Симетрично" if not stack else "Несиметрично"


if __name__ == "__main__":
    examples = ["( ){[ 1 ]( 1 + 3 )( ){ }}", "( 23 ( 2 - 3);", "( 11 }"]

    for example in examples:
        result = check_brackets(example)
        print(f"{example}: {result}")
