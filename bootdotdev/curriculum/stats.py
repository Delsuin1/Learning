def sort_on(word: tuple[str, int]) -> int:
    return word[1]

def dict_sorted_list(dict_tuple: dict[str,int]) -> list[tuple[str,int]]:
    dict_list = []
    
    for key in dict_tuple:
        value = dict_tuple[key]
        dict_list.append(((key,value)))
    sorted_list = sorted(dict_list, reverse=True, key = sort_on)
    
    return sorted_list

def count_words(text: str) -> int:
    word_count = len(text.split())
    return word_count


def count_letters(text:str) -> dict:
    dict_character = {}
    text = text.lower()
    for i in text: 
        dict_character[i] = dict_character.get(i,0) +1
    return dict_character

# word = "aaaaaabbbccccddefgggg"
  
# print(count_letters(word))
# print(dict_sorted_list(count_letters(word)))
