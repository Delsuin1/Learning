import sys
from stats import (
    count_words, 
    count_letters, 
    dict_sorted_list
)
if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path = sys.argv[1]
    
def get_book_text(path : str) -> str:
    with open(path) as f:
        return f.read()

def print_report(book_path: str, word_count: int, char_count:list[tuple[str, int]]) -> None:
    print(f"""============ BOOKBOT ============
Analyzing book {book_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    for char, count in char_count: 
        if not char.isalpha():
            continue
        print(f"{char}: {count}")
    print("============= END ===============")
   

def main() -> None:
    book_path = path
    words = get_book_text(book_path)
    word_count = count_words(words)
    word_dict = count_letters(words)
    sorted_count = dict_sorted_list(word_dict)
    print_report(f"found at {book_path}", word_count, sorted_count)

main()