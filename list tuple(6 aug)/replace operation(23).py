import re

input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")
target = input("Enter the word or phrase to find: ")
replacement = input("Enter the replacement word or phrase: ")

choice = input("Case-sensitive replacement? (yes/no): ")

try:

    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()
    if choice.lower() == "yes":
       
        modified_text = text.replace(target, replacement)
    else:
        modified_text = re.sub(
            re.escape(target),
            replacement,
            text,
            flags=re.IGNORECASE
        )

    
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(modified_text)

    print("\nFind-and-replace completed successfully.")
    print("Modified file saved as:", output_file)

except FileNotFoundError:
    print("Error: The input file was not found.")
except Exception as e:
    print("An error occurred:", e)
