

if __name__ == "__main__":
    def filter_letters(input_string):
        for char in input_string:
            if not char.isalpha():
                return "ошибка, введите только латинские буквы"
        letter_counts = {}
        for char in input_string:
            small_char = char.lower()

            if small_char not in letter_counts:
                letter_counts[small_char] = [0, 0]
            if char.islower():
                letter_counts[small_char][0] += 1
            else:
                letter_counts[small_char][1] += 1
        result = []
        for char in input_string:
            small_char = char.lower()
            small_count, big_count = letter_counts[small_char]
            if small_count <= big_count:
                result.append(char)
        return ''.join(result)

    print(filter_letters(input('-->')))

