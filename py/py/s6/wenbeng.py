def analyze_text(text):
    char_count = {}
    for char in text:
        if char.isalnum():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

text = "Hello, World!"
print(analyze_text(text))