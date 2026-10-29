# string_utils.py

def count_vowels(s):
    count = 0
    for ch in s:
        if ch.lower() in "aeiou":
            count += 1
    return count


def reverse_string(s):
    return s[::-1]


def is_palindrome(s):
    return s == s[::-1]


def count_words(s):
    return len(s.split())


def remove_spaces(s):
    return s.replace(" ", "")
