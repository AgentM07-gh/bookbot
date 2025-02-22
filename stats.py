def word_count(str):
    word_total = 0
    word_list = str.split()
    for words in word_list:
        word_total += 1
    return word_total

def character_count(str):
    char_cnt_dict = {}
    str_lower = str.lower()
    for chars in str_lower:
        if chars not in char_cnt_dict:
            char_cnt_dict.update({chars:1})
        else:
            char_cnt_dict[chars] += 1
    return char_cnt_dict

def sort_on(dict):
    return dict["count"]

def sorted_char_count(char_cnt_dict):
    char_cnt_list = []
    for char, count in char_cnt_dict.items():
        char_cnt_list.append({"character": char, "count": count})
    char_cnt_list.sort(reverse=True, key=sort_on)
    return char_cnt_list

