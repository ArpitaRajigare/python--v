import string

def normalize(text):
    text = text.lower()
    return ''.join(char for char in text if char.isalnum())

def frequency(text):
    count = {}
    for char in text:
        count[char] = count.get(char, 0) + 1
    return count

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

string1 = normalize(string1)
string2 = normalize(string2)

if frequency(string1) == frequency(string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
