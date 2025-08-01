def is_palindrome(word):
    return word == word[::-1]

word = input("Enter a word:")
print(f"{word} is a palindrome!" if is_palindrome(word) else "Not a Palindrome,")