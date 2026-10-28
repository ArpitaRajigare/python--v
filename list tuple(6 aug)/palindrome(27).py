
import re


text = input("Enter a word or phrase: ")

normalized_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
if normalized_text == normalized_text[::-1]:
    print(True)
else:
    print(False)
