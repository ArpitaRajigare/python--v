import re
from collections import Counter

text = input("Enter research paper text:\n")

stopwords = {
    "the", "is", "a", "an", "and", "of", "to", "in",
    "for", "on", "with", "this", "that", "are", "was",
    "as", "by", "from", "be", "or", "it"
}

words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())

keywords = [word for word in words if word not in stopwords]

top5 = Counter(keywords).most_common(5)

print("\nTop 5 Keywords:")
for word, count in top5:
    print(word, ":", count)
