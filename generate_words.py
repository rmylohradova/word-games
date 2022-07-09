from dict import words


def txt_to_list(txt_file):
    word_list = []
    with open(txt_file, 'r') as file:
        for line in file:
            word_list.append(line.strip())
    return word_list


def complete_wordle_words():
    sgb_list = txt_to_list('sgb-words.txt')
    wrdl_words = [word for word in words if len(word) == 5]
    wrdl_words = wrdl_words + sgb_list
    return wrdl_words

