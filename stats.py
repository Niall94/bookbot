def get_word_count(book):
    words = book.split()
    return len(words)

def character_count(text):
    text_lower = text.lower()
    char_split = list(text_lower)
    char_count = 0
    char_dict = {}
    for char in char_split:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_count = 0
            char_count += 1
            char_dict[char[0]] = char_count

    return char_dict

def get_sorted_dict(text):
    num_list = []
    char_dict = character_count(text)
    sorted_dict = {}
    for char in char_dict:
        if char.isalpha() == True:
            num = char_dict[char]
            sorted_dict[char] = num


    return dict(sorted(sorted_dict.items(), key=lambda item: item[1], reverse=True))