from collections import deque


def is_palindrome(text):
    clean_text = "".join(c.lower() for c in text if c.isalnum())
    d = deque(clean_text)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


if __name__ == "__main__":
    examples = ["Racecar", "A man a plan a canal Panama", "Not a palindrome"]

    for example in examples:
        result = is_palindrome(example)
        print(f"'{example}' → {'паліндром' if result else 'не паліндром'}")
