import re

def extract_phone_numbers(text):
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    phone_numbers = re.findall(pattern, text)
    return phone_numbers

if __name__ == "__main__":
    sample_text = """
    Please contact our departments using the numbers below:
    - Customer Support: (123) 456-7890
    - Technical Line: 123-456-7890
    - Billing Department: 123.456.7890
    - Direct Line: 1234567890
    
    (Note: Invalid numbers like 12-345-6789 or 12345 will be correctly ignored.)
    """
    
    extracted_numbers = extract_phone_numbers(sample_text)
    
    for number in extracted_numbers:
        print(number)