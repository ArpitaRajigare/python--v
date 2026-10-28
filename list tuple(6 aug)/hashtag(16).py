import re

def extract_hashtags(text):
    pattern = r'#[A-Za-z0-9_]+'

  
    hashtags = re.findall(pattern, text)

    return hashtags

text = input("Enter a social media post: ")
hashtags = extract_hashtags(text)

print("Extracted hashtags:")
print(hashtags)
