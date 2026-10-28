import re

dictionary = {"this", "is", "a", "simple", "python", "program",
              "spell", "checker", "hello", "world", "book", "library"}

text = input("Enter text: ")

words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

misspelled = [word for word in words if word not in dictionary]

print("Misspelled words:", misspelled)
