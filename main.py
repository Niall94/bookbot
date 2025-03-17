import sys
from stats import get_word_count, character_count, get_sorted_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    
    text = get_book_text(path)
    num_words = get_word_count(text)
    char_dict = character_count(text)
    sorted_dict = get_sorted_dict(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_dict:
        num = sorted_dict[char]
        print(f"{char}: {num}")

main()