def validate_DuplicatedStrings(StringInput):
    result = set()  
    seen_chars = set()

    for string in StringInput:
        for char in string:
            if char in seen_chars:
                result.add(char)
            else:
                seen_chars.add(char)

    return list(result)

input_strings = ['abcdef', 'bcdefg', 'cdefgh']
duplicates = validate_DuplicatedStrings(input_strings)
print("Duplicate characters:", duplicates)
