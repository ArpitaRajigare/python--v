def count_character_frequency():
    text = input("Enter a string: ")
    case_sensitive = input("Case-sensitive? (y/n): ").strip().lower() == 'y'
    
    if not case_sensitive:
        text = text.lower()
        
   
    freq_dict = {}
    for char in text:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    
    sorted_freq = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
    
    print("\nCharacter Frequencies (Descending Order):")
    for char, count in sorted_freq:
        display_char = "' '" if char == ' ' else f"'{char}'"
        print(f"{display_char}: {count}")

if __name__ == "__main__":
    count_character_frequency()