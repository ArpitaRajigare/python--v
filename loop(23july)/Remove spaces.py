s = input("Enter a string: ")

new = ""

for ch in s:
    if ch != " ":
        new += ch

print("String without spaces:", new)