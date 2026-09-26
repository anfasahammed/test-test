def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    word = input("Enter a string: ")
    if is_palindrome(word):
        print(f"'{word}' is a palindrome")
    else:
        print(f"'{word}' is not a palindrome")
