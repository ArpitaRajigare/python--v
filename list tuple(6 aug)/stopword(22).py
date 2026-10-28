import re

stopwords = {
    "is", "am", "are", "was", "were", "the", "a", "an",
    "and", "or", "but", "in", "on", "at", "to", "of",
    "for", "with", "this", "that", "it", "as", "by", "from"
}

text = input("Enter a paragraph: ")
words = text.split()

cleaned_words = []

for word in words:
    clean_word = re.sub(r'^[^\w]+|[^\w]+$', '', word)
    
    if clean_word.lower() not in stopwords:
        cleaned_words.append(word)
cleaned_text = " ".join(cleaned_words)

print("\nCleaned Text:")
print(cleaned_text)
