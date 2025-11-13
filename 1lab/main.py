
if __name__ == "__main__":
    text = input("-->")
    text = text.lower()
    words = text.split()
    letters_count = {}
    for char in text:
        if char.isalpha():
            if char in letters_count:
                letters_count[char] += 1
            else:
                letters_count[char] = 1
    words_count = {}
    for word in words:
        clean_word = ""
        for char in word:
            if char.isalpha():
                clean_word += char
    
        if clean_word:
            if clean_word in words_count:
                words_count[clean_word] += 1
            else:
                words_count[clean_word] = 1
    
    
    letters_sorted = sorted(letters_count.items(), key=lambda x: x[1], reverse=True)
    words_sorted = sorted(words_count.items(), key=lambda x: x[1], reverse=True)
    
    print("\nТоп-5 самых частых букв:")
    for i in range(min(5, len(letters_sorted))):
        letter, count = letters_sorted[i]
        print(f"{i + 1}. Буква '{letter}' - {count} раз")
    
    print("\nТоп-5 самых частых слов:")
    for i in range(min(5, len(words_sorted))):
        word, count = words_sorted[i]
        print(f"{i + 1}. Слово '{word}' - {count} раз")
