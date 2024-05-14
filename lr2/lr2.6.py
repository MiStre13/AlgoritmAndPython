def count_characters_occurrences(input_string):
    char_occurrences = {}
    
    for char in input_string:
        if char in char_occurrences:
            char_occurrences[char] += 1
        else:
            char_occurrences[char] = 1
    
    return char_occurrences



input_string = input("Введите строку: ")
result = count_characters_occurrences(input_string)
for char, count in result.items():
    print(f"Символ '{char}' встречается {count} раз")
